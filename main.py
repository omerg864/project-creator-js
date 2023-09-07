import os
import platform

useRoute = []

def expressBaseCreate(backend_name, main_dir):
    os.mkdir(backend_name)
    os.chdir(backend_name)
    os.mkdir('controllers')
    os.mkdir('models')
    os.mkdir('routes')
    os.mkdir('config')
    os.mkdir('middleware')
    open("server.js", "w").write(open(main_dir +"/serverImports.txt", "r").read())
    open(".env", "w").write("NODE_ENV=development\nPORT=5000\nMONGO_URI=''")
    open(".gitignore", "w").write(".env\nnode_modules\n.DS_Store\npackage-lock.json\n")
    os.chdir('config')
    db = open("db.js", "w")
    db_txt = open(main_dir + "/db.txt", "r")
    db.write(db_txt.read())
    os.chdir('..')


def expressCollectionCreate(collection, main_dir):
    model_txt = open(main_dir + "/model.txt", "r")
    route_txt = open(main_dir + "/route.txt", "r")
    controller_txt = open(main_dir + "/controller.txt", "r")
    capitalized_collection = collection[0].upper() + collection[1:]
    lower_collection = collection[0].lower() + collection[1:]
    os.chdir('models')
    open(collection + "Model"  + ".js", "w").write(model_txt.read().replace("-model_name-", lower_collection).replace("-model_name-", capitalized_collection)
    .replace("-model_name-", lower_collection))
    os.chdir('..')
    os.chdir('routes')
    open(collection + "Routes" + ".js", "w").write(route_txt.read().replace("-name-", capitalized_collection))
    os.chdir('..')
    os.chdir('controllers')
    open(collection + "Controller" + ".js", "w").write(controller_txt.read().replace("-name-", capitalized_collection).replace("-name-", lower_collection)
    .replace("-name-", capitalized_collection).replace("-name-", lower_collection).replace("-name-", capitalized_collection).replace("-name-", lower_collection)
    .replace("-name-", lower_collection).replace("-name-", capitalized_collection))
    model_txt.close()
    route_txt.close()
    controller_txt.close()
    os.chdir('..')
    useRoute.append(f'\napp.use("/api/{lower_collection}", {lower_collection}Router);')
    importName = "\nimport " + lower_collection + "Router from './routes/" + lower_collection + "Routes.js';"
    open("server.js", "a").write(importName)

def nestCollectionCreate(collection):
    os.system('cmd /c "nest g mo ' + collection + "\"")
    os.system('cmd /c "nest g co ' + collection + "\"")
    os.system('cmd /c "nest g s ' + collection + "\"")

def main():
    main_dir = os.getcwd() + "/src"
    project_name = input('Project name: ')
    os.mkdir(project_name)
    os.chdir(project_name)
    backend_name = input('Backend name: ')
    backend_type = input('Backend type: (options: nest, express) \n (default: ExpressJS)')
    if backend_type == 'express' or backend_type == '':
        expressBaseCreate(backend_name, main_dir)
    else:
        os.system('cmd /c "nest new ' + backend_name + "\"")
    collections = []
    input_collection = ""
    while input_collection != "q":
        input_collection = input('Enter Collection Name: (To Stop Enter q)')
        if input_collection != "q":
            collections.append(input_collection)
    frontend = input('Create frontend as well? (yes)')
    if frontend == 'yes' or frontend == '':
        frontend = True
    else:
        frontend = False
    choiceFrontend = ''
    if frontend:
        frontend_name = input('Frontend name: ')
        choiceFrontend = input('Choose frontend framework: \n (options: vue, react)\n (default: react)')
        if choiceFrontend != 'vue':
            typescript = input('Use typeScript template? (yes)')
    for collection in collections:
        if backend_type == 'express' or backend_type == '':
            expressCollectionCreate(collection, main_dir)
        else:
            os.system('cmd /c "cd ' + backend_name + "\"")
            nestCollectionCreate(collection)
    if backend_type == 'express' or backend_type == '':
        serverJS = open("server.js", "a")
        serverJS.write("\n\n")
        serverJS.write(open(main_dir +"/serverBase.txt", "r").read())
        for route in useRoute:
            serverJS.write(route)
        serverJS.write(open(main_dir +"/serverProd.txt", "r").read())
        serverJS.close()
        os.chdir('middleware')
        open("errorMiddleware.js", "w").write(open(main_dir + "/errorMid.txt", "r").read())
        os.chdir('..')
        if platform.system() == 'Windows':
            os.system('cmd /c "npm init"')
            os.system('cmd /c "npm install dotenv express mongoose express-async-handler"')
            os.system('cmd /c "npm install -D nodemon concurrently"')
        else:
            os.system("sudo npm init")
            os.system("sudo npm install dotenv express mongoose express-async-handler")
            os.system("sudo npm install -D nodemon concurrently")
    else:
        if platform.system() == 'Windows':
            os.system('cmd /c "npm install dotenv mongoose"')
            os.system('cmd /c "cd .."')
        else:
            os.system("sudo npm install dotenv mongoose")
            os.system('cmd /c "cd .."')
    if frontend:
        os.chdir('..')
        if choiceFrontend != 'vue':
            if typescript == 'yes' or typescript == '':
                if platform.system() == 'Windows':
                    os.system("cmd /c \"npx create-react-app " + frontend_name + " --template typescript\"")
                else:
                    os.system("sudo npx create-react-app " + frontend_name + " --template typescript")
            else:
                if platform.system() == 'Windows':
                    os.system("cmd /c \"npx create-react-app " + frontend_name + "\"")
                else:
                    os.system("sudo npx create-react-app " + frontend_name)
        else:
            if platform.system() == 'Windows':
                os.system("cmd /c \"vue create " + frontend_name + "\"")
            else:
                os.system("sudo vue create " + frontend_name)



if __name__ == '__main__':
    main()
    print('Created Project')