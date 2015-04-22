# Author: Regan McCooey
# Date: 2/6/15
# Class: CSCI 356 Professor Walsh
# Assignment: Project 1 - Websocket
# Purpose: to build a websocket in python

import sys
import socket
import datetime
import threading


def main():

    # handle the arguments passed into the terminal
    if len(sys.argv) != 3:
        print 'please enter a port number and a directory name!'
        sys.exit(1)

    port_num = int(sys.argv[1])
    direct_name = sys.argv[2]
    

    # bind the socket
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    sock.bind( ('', port_num) )
    sock.listen(5)
    

    
    while True:
        conn, addr = sock.accept()
        th = threading.Thread( target = send_web_data, args = ( conn, direct_name ) )
        th.start()





def send_web_data( conn, direct_name ):
    try:
        message = conn.recv(1024)
    except Exception as r:
        print 'an error has occured: ' + r

    print message

    # split up the message 
    method, path, ver, garbage = message.split(None, 3)

    if method == 'GET':

        # handle hello 
        if path == '/hello':

            hello_msg = 'Hello! How are you today? Today is ' + str(datetime.date) +' and it is ' + str(datetime.time) +'\r\n'
            conn.sendall( 'HTTP/1.1 200 OK\r\n'+ 
            'Date: '+str(datetime.datetime.now())+'\r\n'+
            'Server: rmmcco16\r\n'+
            'Content-Length:' + str(len(hello_msg)) + '\r\n' +
            'Content-Type: text/plain\r\n' + hello_msg ) 

        # handle static content
        else :

            # change default path to index.html
            if path == '/': 
                path = '/index.html'

            # open the file using the path and the directory name
            try:
                print 'attempting to open: '+ direct_name+path
                file = open(direct_name+path,'r')
            except Exception as e:
                print 'FILE NOT FOUND\n'
                conn.send('HTTP/1.1 404')
                sys.exit(1)

            # read the data in the file, generate an okay response and send the data from the file over
            data = file.read()
            msg = gen_ok_response(data, direct_name+path)
            print 'message: ' + msg
            conn.sendall(msg)
            conn.sendall(data +'\r\n')
            print 'OK sent'

            conn.close()       


# pre: data and file_path both exist
# post: a message for the static content is generated
def gen_ok_response(data, file_path):

    # generate string for message
    ok_str = 'HTTP/1.1 200 OK\r\n' 
    date = 'Date: ' + str(datetime.datetime.now()) +'\r\n'
    server = 'Server: rmmcco16\r\n' 
    content_len ='Content-Length: '+ str(len(data)) +'\r\n'
    connection = 'Connection: close\r\n' 

    # get the type of content 
    type = get_file_type(file_path) 

    # error checking if that type is not handled 
    if type == -1:
        print 'ERROR: FILE TYPE NOT SUPPORTED\n'
        sys.exit(1)

    content_type = 'Content-Type: '+ type +'\r\n\r\n' 

    return ok_str + date + server + content_len + connection + content_type


# pre: the file path exists
# post: the content type will be returned, if the content type does not exist, -1 will be returned
def get_file_type(file_path):

    ext = file_path[-4:]
    ext = ext.lower()
    if ext == 'jpeg' or ext == '.jpg':
        type = 'image/jpeg'
    elif ext == 'html':
        type = 'text/html'
    elif ext == '.txt':
        type = 'text/plain'
    elif ext == '.css':
        type = 'text/css'
    elif ext == '.gif':
        type = 'image/gif'
    elif ext == '.png':
        type = 'image/png'
    elif ext == 'woff':
        type = 'application/x-font-woff'
    else:
        new_ext = file_path[-2:]
        print 'looking at extension: '+new_ext
        if new_ext == 'js':
            type = 'application/javascript'
        else:
           return -1
    print 'Type returned: '+type
    return type
    
if __name__ == '__main__':
    main()
