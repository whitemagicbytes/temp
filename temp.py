import os
import yaml

# GitHub organization name
organization_name = 'your_organization'

# Directory where repositories will be cloned
clone_directory = 'path/to/cloned/repositories'

def get_organization_repositories(org_name, token):
    # Ensure the clone directory exists
    os.makedirs(clone_directory, exist_ok=True)

    # GitHub API URL for organization repositories
    url = f'https://api.github.com/orgs/{org_name}/repos'

    # Use curl with Bearer token for authentication and print the output
    os.system(f'curl -s -H "Authorization: Bearer {token}" {url} > repositories.json')

    # Parse the repositories.json file and clone each repository
    with open('repositories.json', 'r') as file:
        repositories = yaml.safe_load(file)

        # Clone each repository using git command
        for repo in repositories:
            repo_name = repo['name']
            os.system(f'git clone git@github.com:{org_name}/{repo_name}.git {os.path.join(clone_directory, repo_name)}')

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


def update_yaml_file(file_path, yaml_to_compare_path):
    try:
        # Load YAML data from both files
        with open(file_path, 'r') as file:
            yaml_data = yaml.safe_load(file)

        with open(yaml_to_compare_path, 'r') as file:
            yaml_to_compare_data = yaml.safe_load(file)

        # Check if the 'secrets' key exists in YAML 1
        if 'secrets' in yaml_data:
            # Check if 'valut_paths' key exists in YAML 1
            if 'valut_paths' in yaml_data['secrets'][0]:
                # Update 'valut_paths' in YAML 1 with the value from YAML 2
                yaml_data['secrets'][0]['valut_paths'] = yaml_to_compare_data.get('valut_paths', [])

                # Write the modified YAML data back to the file
                with open(file_path, 'w') as file:
                    yaml.dump(yaml_data, file, default_flow_style=False)

                print(f'Updated "valut_paths" in "{file_path}" with values from "{yaml_to_compare_path}"')
                return True
            else:
                print(f'Key "valut_paths" not found in "{file_path}"')
        else:
            print(f'Key "secrets" not found in "{file_path}"')

        return False
    except Exception as e:
        print(f'Error updating YAML file: {str(e)}')
        return False
