VERSION ?= latest
IMAGE_NAME = elt-pipeline

build:
	docker build -t $(IMAGE_NAME):$(VERSION) .

run:
	docker compose up -d

down:
	docker compose down --volumes --remove-orphans

clean:
	docker system prune -af --volumes

list:
	docker image ls | grep $(IMAGE_NAME)

tag:
	@echo "🧱 Versionando imagem: $(IMAGE_NAME):$(VERSION)"
	docker tag $(IMAGE_NAME):latest $(IMAGE_NAME):$(VERSION)