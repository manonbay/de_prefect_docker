from prefect.infrastructure.container import DockerContainer

# alternative to creating DockerContainer block in the UI
docker_block = DockerContainer(
    image="hapalochlaena/dockerprefect:zoomcamp",  # insert your image here
    image_pull_policy="ALWAYS",
    auto_remove=True,
)

docker_block.save("dockerprefect", overwrite=True)
