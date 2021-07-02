test:
	docker build -f dev.Dockerfile -t miniflask-test .
	docker run --privileged -v /lib/modules:/lib/modules --entrypoint "/bin/sh" miniflask-test -c /root/toynet-mininet/test-entrypoint.sh
