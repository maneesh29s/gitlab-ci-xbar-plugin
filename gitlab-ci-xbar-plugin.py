#!/usr/bin/python3

#  <xbar.title>Gitlab CI Xbar Plugin</xbar.title>
#  <xbar.version>v0.1.0</xbar.version>
#  <xbar.author>Maneesh Sutar</xbar.author>
#  <xbar.author.github>maneesh29s</xbar.author.github>
#  <xbar.desc>Monitor gitlab ci pipelines</xbar.desc>
#  <xbar.dependencies>python3, pyyaml, requests</xbar.dependencies>

import yaml
import requests
import os

CONFIG_PATH=os.path.join(os.getenv('HOME'),"gitlab-ci-xbar-plugin.yaml")

class Project:
    """
    A data object for holding project level information
    """
    def __init__(self, name, id, branches):
        """
        The constructor

        Parameters
        ----------
        name: Name of the pipeline
        id: ID of the pipeline
        branches: Branches to track
        """
        self.name = name
        self.id = id
        self.branches = branches
        self.pipelines = []


class Pipeline:
    """
    A data object for holding project level information
    """
    def __init__(self, ref, id, status, url) -> None:
        self.ref = ref
        self.id = id
        self.status = status
        self.url = url


if __name__ == "__main__":
    projects = []
    pipelines = []

    with open(CONFIG_PATH, "r") as config_file:
        config = yaml.safe_load(config_file)


    projects_from_yaml = config['projects']


    for project in projects_from_yaml:
        projects.append(Project(project['name'], project['id'], project['branches']))

    ANY_PIPELINE_RED=False

    for project in projects:
        for branch in project.branches:
            req = f"{config['GITLAB_ENDPOINT']}/projects/{project.id}/pipelines/latest?ref={branch}"
            res = requests.get(req).json()

            if res['status'] == "failed":
                ANY_PIPELINE_RED=True

            project.pipelines.append(Pipeline(res['ref'], res['id'], res['status'], res['web_url']))

    if ANY_PIPELINE_RED:
        print("🛑")
    else:
        print("🟢")

    print("---")

    for project in projects:
        if project.pipelines:
            print(f"{project.name}")
            for pipeline in project.pipelines:
                if pipeline.status == "success":
                    style = "green"
                elif pipeline.status == "running":
                    style = "yellow"
                else:
                    style = "red"

                print(f"-- {pipeline.ref} | href={pipeline.url} | color={style}")