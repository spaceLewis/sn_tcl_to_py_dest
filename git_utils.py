

import git

def get_git_repo():
    try:
        return git.Repo(search_parent_directories=True)
    except git.exc.InvalidGitRepositoryError:
        raise ValueError("Invalid Git repository")

def get_current_branch():
    repo = get_git_repo()
    try:
        return repo.active_branch.name
    except AttributeError:
        raise ValueError("Failed to retrieve current branch")

def get_current_commit():
    repo = get_git_repo()
    try:
        return repo.head.commit.hexsha
    except AttributeError:
        raise ValueError("Failed to retrieve current commit")

try:
    currentBranch = get_current_branch()
    currentCommit = get_current_commit()
except ValueError as e:
    print(f"Error: {e}")