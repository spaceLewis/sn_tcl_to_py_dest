

import git
import os

def check_git_branch_and_commit():
    try:
        repo = git.Repo(search_parent_directories=True)
        if not repo:
            raise Exception("Git repository not found")
        branch = repo.active_branch
        commit = repo.head.commit
        if repo.is_dirty():
            raise Exception("Git repository is dirty")
        return branch.name, commit.hexsha
    except git.exc.InvalidGitRepositoryError:
        raise Exception("Invalid Git repository")
    except git.exc.NoSuchPathError:
        raise Exception("Git repository path not found")
    except Exception as e:
        raise Exception("Error checking Git branch and commit: " + str(e))