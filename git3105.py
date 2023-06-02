import time

from git import Repo
import git
import datetime
from datetime import datetime


def getRepo():
    print("Executing get repo function")
    repo_path = "D:\\Pushkar\\GIT\\"  # setting up repo path on local machine
    repo = Repo(repo_path)
    git.Git(repo_path).clone("https://github.com/pushkarnagarkar/newgitrepo.git")  # cloning the remote repo on local
    # machine at the given path


def createNewBranch():
    now = datetime.now()
    date_time = now.strftime("%m-%d-%y-%H-%M-%S")
    repo_path = "D:\\Pushkar\\GIT\\newgitrepo\\"
    repo = Repo(repo_path)
    new_branch = 'execution_' + date_time
    # new_branch = 'temp3'
    current = repo.create_head(new_branch)
    print("New branch created ==> " + new_branch)
    current.checkout()
    repo.git.push('--set-upstream', "https://github.com/pushkarnagarkar/newgitrepo.git", new_branch)
    print("Branch" + new_branch + "committed to remote")


def pushToGit():
    repo_path = "D:\\Pushkar\\GIT\\newgitrepo\\"
    repo = Repo(repo_path)
    repo.git.add('D:\\Pushkar\\GIT\\newgitrepo\\')
    repo.git.commit('-m', 'commit message from pushkar')
    origin = repo.remote(name='origin')
    origin.push()
    print("files pushed to remote")


def attachDateTime():
    # branch_name = "execution" + "_" + str(datetime.date.today())
    branch_name = "execution" + "_"
    now = datetime.now()
    date_time = now.strftime("%m-%d-%y")
    print(date_time)
    new_branch = 'execution' + date_time
    print(type(new_branch))

    print(date_time)
    print(now)
    # currenttimestamp = datenow + "_" + str(datetime.date.today())
    # print(currenttimestamp)

    # mylist = []
    # for i in range(5):
    #     currenttimestamp = datenow + "_" + str(datetime.date.today()) + "{}".format(datetime.datetime.now().strftime("%H:%M:%S"))
    #     mylist.append(currenttimestamp)
    # print(mylist)


# def getBranchList():
#     repo_path = "D:\\Pushkar\\GIT\\newgitrepo\\"
#     repo = Repo(repo_path)
#     repo = git.Repo('.')
#     remote_refs = repo.remote().refs
#     # current_branch = repo.active_branch.name
#     for refs in remote_refs:
#         print(refs.name)


def getBranchList():
    r = Repo("D:\\Pushkar\\GIT\\newgitrepo\\")
    repo_heads = r.heads
    repo_head_names = [h.name for h in repo_heads]
    for i in repo_head_names:
        print(i)

    

# getRepo()
# createNewBranch()
# pushToGit()
# attachDateTime()
getBranchList()
