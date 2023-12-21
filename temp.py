import os
import yaml

# GitHub organization name
organization_name = 'your_organization'

# Directory where repositories will be cloned
clone_directory = 'path/to/cloned/repositories'

def get_organization_repositories(org_name):
    url = f'git@github.com:{org_name}.git'
    os.system(f'git clone {url} {clone_directory}')

def create_pull_request(repo_name, base_branch, head_branch, title, body):
    os.system(f'cd {clone_directory}/{repo_name} && git checkout -b {head_branch} && git push origin {head_branch}')
    os.system(f'cd {clone_directory}/{repo_name} && git checkout {base_branch}')
    os.system(f'cd {clone_directory}/{repo_name} && git pull origin {base_branch}')
    os.system(f'cd {clone_directory}/{repo_name} && git merge --no-ff {head_branch}')
    os.system(f'cd {clone_directory}/{repo_name} && git push origin {base_branch}')
    os.system(f'cd {clone_directory}/{repo_name} && git checkout {base_branch}')
    os.system(f'cd {clone_directory}/{repo_name} && git branch -D {head_branch}')

def update_yaml_file(file_path, key_to_update, new_value):
    try:
        # Load YAML data from the file
        with open(file_path, 'r') as file:
            yaml_data = yaml.safe_load(file)

        # Update the specified key with the new value
        yaml_data[key_to_update] = new_value

        # Write the modified YAML data back to the file
        with open(file_path, 'w') as file:
            yaml.dump(yaml_data, file, default_flow_style=False)

        print(f'Value for key "{key_to_update}" updated successfully in {file_path}')
        return True
    except Exception as e:
        print(f'Error updating YAML file: {str(e)}')
        return False

def delete_line_in_yaml(file_path, string_to_delete):
    try:
        # Read the contents of the YAML file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Remove lines containing the specified string
        modified_lines = [line for line in lines if string_to_delete not in line]

        # Write the modified lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(modified_lines)

        print(f'Lines containing "{string_to_delete}" deleted successfully in {file_path}')
        return True
    except Exception as e:
        print(f'Error deleting lines in YAML file: {str(e)}')
        return False

# Get all repositories in the organization
get_organization_repositories(organization_name)

# Lists to store success and failure details
success_list = []
failure_list = []

# Iterate through each repository and create a new pull request
for repo_name in os.listdir(clone_directory):
    base_branch = 'master' if os.path.exists(os.path.join(clone_directory, repo_name, 'master')) else 'main'
    head_branch = 'newchanges'
    title = 'New Changes'
    body = 'This is a new pull request with some changes.'

    # Update a YAML file in the cloned repository (replace these values with your own)
    yaml_file_path = os.path.join(clone_directory, repo_name, 'path/to/your/file.yaml')
    key_to_update = 'your_key'
    new_value = 'your_new_value'

    # Update YAML file and track success/failure
    if update_yaml_file(yaml_file_path, key_to_update, new_value):
        success_list.append(repo_name)
    else:
        failure_list.append(repo_name)

    # Delete a line containing a specific string in the YAML file (replace these values with your own)
    string_to_delete = 'string_to_delete'
    if delete_line_in_yaml(yaml_file_path, string_to_delete):
        print(f'Lines containing "{string_to_delete}" deleted successfully in {yaml_file_path}')

    # Create a pull request
    try:
        create_pull_request(repo_name, base_branch, head_branch, title, body)
        print(f'Pull request created successfully in {repo_name}.')
    except Exception as e:
        print(f'Error creating pull request in {repo_name}: {str(e)}')

# Generate and print the report
print("\n----- Update Report -----\n")
print("Repositories updated successfully:")
for repo_name in success_list:
    print(f"- {repo_name}")

print("\nRepositories update failed:")
for repo_name in failure_list:
    print(f"- {repo_name}")
