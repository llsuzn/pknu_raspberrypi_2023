#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define BUF_SIZE 2048
#define IMG_BUF_SIZE 500000
void error_handling(char *message);

char buffer[BUF_SIZE];
char img_buffer[IMG_BUF_SIZE];

char message[] = "HTTP/1.1 200 OK\r\n"
                 "Server:Linux Web Server\r\n"
                 "Content-Type : text/html; charset=UTF-8\r\n\r\n"
                 "<!DOCTYPE html>\r\n"
                 "<html><head><title> My Web Page </title>\t\n"
                 "<style>body {background-color: #FFFF00 }</style></head>\r\n"
                 "<body><center><h1>Hello World!</h1><br>\r\n"
								 "<img src=\"image.jpg\"></center></body></html>\r\n";
int main(int argc, char *argv[])
{
	int fdimg=0;
	int serv_sock, clnt_sock;

	struct sockaddr_in serv_adr, clnt_adr;
	socklen_t clnt_adr_sz;

	if(argc!=2)
	{
		printf("Usage : %s <port>\n",argv[0]);
		exit(1);
	}

	serv_sock=socket(PF_INET,SOCK_STREAM,0);
	if(serv_sock==-1)
		error_handling("socket() error");

	memset(&serv_adr,0,sizeof(serv_adr));
	serv_adr.sin_family=AF_INET;
	serv_adr.sin_addr.s_addr=htonl(INADDR_ANY);
	serv_adr.sin_port=htons(atoi(argv[1]));

	if(bind(serv_sock, (struct sockaddr*)&serv_adr,sizeof(serv_adr))==-1)
		error_handling("bind() error");

	if(listen(serv_sock,5)==-1)
		error_handling("listen() error");

	clnt_adr_sz=sizeof(clnt_adr);

	while(1)
	{
		clnt_sock=accept(serv_sock,(struct sockaddr*)&clnt_adr, &clnt_adr_sz);
		if(clnt_sock==-1)
			error_handling("accept() error");
		else
			printf("Connected Client\n");

		char str[IMG_BUF_SIZE];
		if(read(clnt_sock,buffer,BUF_SIZE)!=-1)
		{
			if(strstr(buffer, "image.jpg")!=NULL)
			{
				//FILE* fdimg=fopen("image.jpg","rt");
				//read(fdimg,img_buffer,IMG_BUF_SIZE);
				//write(clnt_sock,img_buffer,IMG_BUF_SIZE);
				//send(clnt_sock,img_buffer,strlen(img_buffer),0);
				//printf("두번째%s",buffer);
				//fclose(fdimg);
			}
			else
			{
				//printf("첫번째%s",buffer);
				write(clnt_sock,message,BUF_SIZE);
			}
		}
		close(clnt_sock);
	}
	close(serv_sock);
	printf("-------serv_sock close-------");
	return 0;
}

void error_handling(char *message)
{
	fputs(message,stderr);
	fputc('\n',stderr);
	exit(1);
}
