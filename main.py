import os


def main():
    main_dir = os.getcwd() + "/src"
    project_name = input('Project name: ')
    os.mkdir(project_name)
    os.chdir(project_name)
    os.mkdir('backend')
    os.chdir('backend')
    os.mkdir('controllers')
    os.mkdir('models')
    os.mkdir('routes')
    os.mkdir('config')
    os.mkdir('middleware')
    open("server.js", "w").write(open(main_dir +"/server.txt", "r").read())
    open(".env", "w").write("NODE_ENV=development\nPORT=5000\nMONGO_URI=''")
    open(".gitignore", "w").write(".env\nnode_modules\n.DS_Store\npackage-lock.json\n")
    os.chdir('config')
    db = open("db.js", "w")
    db_txt = open(main_dir + "/db.txt", "r")
    db.write(db_txt.read())
    os.chdir('..')
    collections = []
    input_collection = ""
    while input_collection != "q":
        input_collection = input('Enter Collection Name: (To Stop Enter q)')
        if input_collection != "q":
            collections.append(input_collection)
    frontend = input('Create react app as well? (yes)')
    if frontend == 'yes' or frontend == '':
        frontend = True
    else:
        frontend = False
    redux = input('use redux template? (yes)')
    if redux == 'yes' or redux == '':
        redux = True
    else:
        redux = False
    for collection in collections:
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
    os.chdir('middleware')
    open("errorMiddleware.js", "w").write(open(main_dir + "/errorMid.txt", "r").read())
    os.chdir('..')
    os.chdir('..')
    os.system('cmd /c "npm init"')
    os.system('cmd /c "npm install dotenv express mongoose express-async-handler"')
    os.system('cmd /c "npm install -D nodemon concurrently"')
    if frontend:
        if redux:
            os.system('cmd /c "npx create-react-app frontend --template redux"')
        else:
            os.system('cmd /c "npx create-react-app frontend"')



if __name__ == '__main__':
    main()
    print('Created Project')