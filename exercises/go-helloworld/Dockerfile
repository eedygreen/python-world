FROM golang:alpine
LABEL maintainer="eedy"

WORKDIR /go/src/app

ADD . .

RUN go build -o helloworld

EXPOSE 6111

CMD ["./helloworld"]

