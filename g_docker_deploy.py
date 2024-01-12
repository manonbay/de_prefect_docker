from prefect.deployments import Deployment
from e_parameterized_flow import etl_parent_flow
from prefect.infrastructure.container import DockerContainer

# charger le block crée avec le fichier 6.make_docker_block
docker_block = DockerContainer.load("dockerprefect")

#utilisation de la fonction etl_parent_flow crée dans le fichier  5_parameterized_flow
docker_dep = Deployment.build_from_flow(
    flow=etl_parent_flow,
    name="docker-flow",
    infrastructure=docker_block,
)
if __name__ == "__main__":
    docker_dep.apply()
