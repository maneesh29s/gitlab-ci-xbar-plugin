# Gitlab CI plugin for xbar

This repo contains a [xbar](https://github.com/matryer/xbar) python plugin for checking status of gitlab ci pipielines.

For Linux GNOME users, same functionality can be availed using [Argos](https://github.com/p-e-w/argos)

The plugin reads a YAML config file present in user's home, and determines which pipelines and projects to track.
An example yaml file is given [here](./xbar-gitlab-ci-plugin.yaml)

## Installing the plugin to xbar

1. Clone this repository (assuming you cloned it in home)

2. Change the python executable at the top of the [plugin file](./gitlab-ci-xbar-plugin.py) `#!/usr/bin/python3` to the location of your global/conda python executable.

3. Using the same python, you need to install the dependencies. If you python executable is `/usr/bin/python3`, you can run

    ```bash
    /usr/bin/python3 -m pip install -r requirements.txt
    ```

4. Using the [example yaml config](./gitlab-ci-xbar-plugin.yaml), create your own config and put it in the home folder. Keep the name of the yaml file same i.e. "gitlab-ci-xbar-plugin.yaml".

5. Create a symlink to the xbar plugins folder. The name of the symlink must contain the time internal for refreshing the plugin. For example,

    ```bash
    cd "$HOME/Library/Application Support/xbar/plugins/"
    ln -s "$HOME/gitlab-ci-xbar-plugin/gitlab-ci-xbar-plugin.py"
    mv gitlab-ci-xbar-plugin.py gitlab-ci-xbar-plugin.15m.py
    ```

    With `15m` in the plugin file name, the xbar will refresh the plugin every 15 minutes.
