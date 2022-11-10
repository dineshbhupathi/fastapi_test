import github
g = github.Github("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")
user = g.get_user()
print(user)
repo = user.create_repo("test")

# blob1 = repo.create_git_blob("file-content", "utf-8")
# element1 = github.InputGitTreeElement(path="path-in-repo.ext", mode='100644', type='blob', sha=blob1.sha)
# # you can read file content into blob, here just use str for example
# blob2 = repo.create_git_blob("file-content2", "utf-8")
# element2 = github.InputGitTreeElement(path="folder/path-in-repo.ext", mode='100644', type='blob', sha=blob2.sha)
# head_sha = repo.get_branch('master').commit.sha
# base_tree = repo.get_git_tree(sha=head_sha)
# tree = repo.create_git_tree([element1, element2], base_tree)
# parent = repo.get_git_commit(sha=head_sha)
# commit = repo.create_git_commit("commit_message", tree, [parent])
# master_refs = self.github_repo.get_git_ref('heads/master')
# master_ref.edit(sha=commit.sha)