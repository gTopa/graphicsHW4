from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    script=open(fname,"r")
    prompt=script.readline()
    while(len(prompt)>0):
        if(prompt=="line\n"):
            prompt=script.readline()
            prompt=prompt.split()
            add_edge(points, prompt[0],prompt[1],prompt[2],prompt[3],prompt[4],prompt[5])
        else if(prompt=="ident\n"):
            ident(transform)
        else if(prompt=="scale\n"):
            prompt=script.readline()
            prompt=prompt.split()
            matrix_mult(make_scale(int(prompt[0]),int(prompt[1]),int(prompt[2])),transform)
        else if(prompt=="move\n"):
            prompt=script.readline()
            prompt=prompt.split()
            matrix_mult(make_translate(int(prompt[0]),int(prompt[1]),int(prompt[2])),transform)
        else if(prompt=="rotate\n"):
            prompt=script.readline()
            prompt=prompt.split()
            if(prompt[0]=="x"):
                matrix_mult(make_rotX(int(prompt[1])),transform)
            if(prompt[0]=="y"):
                matrix_mult(make_rotY(int(prompt[1])),transform)
            if(prompt[0]=="z"):
                matrix_mult(make_rotZ(int(prompt[1])),transform)                
        else if(prompt=="apply\n"):
            matrix_mult(transform,points)
        else if(prompt=="display\n"):
            display(screen)
        else if(prompt=="save\n"):
            save_extension(screen,)
        else if(prompt=="quit\n"):
            
