print("Hanoi_Project","Vasu Gupta")

from graphics import *
from time import sleep

# PURPOSE: Used to determine whether the point is inside the rectangle or not 
# PARAMETERS: the mouse coordinate where the user has clicked, the object rectangle in which we have to check 
# RETURN: NONE
def in_Rectangle(pt, rectangle):
    # Returns true if the pt.x and pt.y are in the rectangle
    return (rectangle.getP1().getX() < pt.x < rectangle.getP2().getX() and
            rectangle.getP1().getY() < pt.y < rectangle.getP2().getY() )    

# PURPOSE: Shows the text under the each post showing the Post name AND the disk list 
# PARAMETERS: NONE
# RETURN: NONE
def show_post_info(): 
    for i in range(len(posts)):
        posts[i][2].setText(posts[i][0]+"\n"+str(posts[i][3]))
        # sets the text object under the posts to show the disk list


# PURPOSE: Makes the disk list empty for each of the post  
# PARAMETERS: NONE 
# RETURN: NONE
def reset_posts():
    for post in posts:
        if post[3] == []: continue        
        post[3].pop(0) #makes the disk list empty
        
        
    show_post_info() #Shows the new modified disk list under each post
    

# PURPOSE: Adds the entry object to enter the number of disks and to display RESET and the user entered text
# PARAMETERS: NONE
# RETURN: NONE
def Hanoi_reset(POST_SP, BASE, WIN_W, WIN_H):
    #global N_entry
    
    if N_entry[2].getText().isdecimal(): 
        ''' if this 'if statement' wasn't written, python was throwing an error of base 10..'''
        N_entry[0] = int(N_entry[2].getText())%10
        # The remainder of the entered value when divided by 10 is made the value of number of disks
        
        N_entry[1].setText("RESET\nN: "+str(N_entry[0]))

    #The code in the try CRASHES when there are NO DISKS as disks is not defined at that point 
    try:  #EXECUTED when the there ARE DISKS inserted in the program as 
        if disks != []:
            for i in range(len(disks)):
                disks[i][2].undraw() #Undrawing the rectangle
                disks[i][3].undraw() #Undrawing the line
                reset_posts()
                sleep(0.2)
                
        create_disks(POST_SP, BASE, WIN_W, WIN_H)
    
        
    except:    #RUNS when there are NO DISKS (For the very first time)
        create_disks(POST_SP, BASE, WIN_W, WIN_H)
        



# PURPOSE: Creates a list for 3 Posts containing the identity of the posts (A,B or C), 3 Rectangles for showing the posts, the text object under each post, creates the disk lists for the posts
# PARAMETERS: The Width and Height for the window, the length of the base of the posts, the width and height of each post(which is the same), and the spacing between the posts.
# RETURN:NONE
def create_posts(WIN_W, WIN_H, BASE, POST_W, POST_H, POST_SP):
    global posts
    # [name -> A,B,C, Rectangle(), Text()-> object of text, disklist]
    post_A, post_B, post_C = ['A', None, None, []],['B', None, None, []], ['C', None, None, []]
    posts = [post_A, post_B, post_C]
    for i in range(3):
        # The rectangle for each post is added to the list
        posts[i][1] = Rectangle(Point((POST_SP + i* POST_SP)-(POST_W//2) , WIN_H-BASE-POST_H),    Point((POST_SP + i* POST_SP)+ POST_W//2  , WIN_H-BASE))
        posts[i][1].setFill('brown')
        posts[i][1].draw(win)
        
        # The text object for each post is added to the list  
        posts[i][2] = Text((Point((POST_SP + i* POST_SP) , WIN_H-BASE+20)), posts[i][0]+'\n'+ str(posts[i][3]))
        posts[i][2].draw(win) 
        
        
    reset_posts()
        

# PURPOSE: HELPER FUNCTON: Creates a rectangle and creates the text inside each rectangle
# PARAMETERS: The window, the top-left coordinates of the point from where rectangle gets started, the width and the height of theh rectangle, the text which has to be displayed inside the button
# RETURN: the rectangle button object created 

def button_create(win, x, y, width, height, text):
    width = x + width
    height = y + height
    #Creates rectangle for the button
    button = Rectangle(Point(x,y), Point(width, height)) 
    button.draw(win) 
    #Text inside the button
    text_in_button = Text(Point((x + width) // 2, (y + height) // 2), text)
    text_in_button.draw(win)
    return button # returns the rectangle button object



#PURPOSE: Creates the disks and appends them to a list and appends the disk id's 
#         to the post[0][3] as well and calls show_post_info() 
#PARAMETERS: The post spacing, the height of the bse from the bottom, The width of the window, the height of the window
#RETURN: NONE
def create_disks(POST_SP, BASE, WIN_W, WIN_H):
    global disks
    global win
    global posts
    global N_entry
    
    
    disks = []
    # disks =  [ [ disk_id, post_name, Rectangle, Text ], ... ]
    #           [ [ n-i ,    'A'      , Rect,     Text to display disk id]] 
    
    DISK_H = 15
    DISK_WMAX = POST_SP-10
    DISK_WMIN = 30
    
    if str(N_entry[0]).isdecimal():
        n = int(N_entry[0])%10     # maybe just say that n = N_entry[0]
        n = N_entry[0]
        
        # Used this if-else statement as if the user enters a value 0 or 10,
        # python throws an error saying cannot divide the number by zero
        if n== 0: steps = 0
        else: steps = (DISK_WMAX - DISK_WMIN) // n  
        
                
        for i in range(n): 
            
            posts[0][3].append(int(n)-i)
            
            disks.append([])
            disks[i].append(str(int(n)-i))           # NOTE: The appended value is a string     
            disks[i].append('A')
            
            
            disks[i].append(Rectangle(Point( POST_SP- (DISK_WMAX//2) +(steps//2)*i , (WIN_H-BASE-DISK_H)-i*DISK_H ),    Point( POST_SP+(DISK_WMAX//2)-(steps//2)*i , (WIN_H-BASE)-i*DISK_H)))
            disks[i][2].setFill('yellow')
            disks[i][2].draw(win)
            
            
            disks[i].append(Text(Point((disks[i][2].getP1().x +disks[i][2].getP2().x)//2, (disks[i][2].getP1().y + disks[i][2].getP2().y)//2) , disks[i][0] ))
            disks[i][3].draw(win)

            show_post_info()
            
            sleep(0.2)  #           '''Not sure whether I should add it here or in the show_post_info()'''
        

# PURPOSE: The function calls the create button function to create the buttons for QUIT and RESET, creates the Entry list which contains the text, the text object and the Entry textbox. 
#          Creates the line for the base of the posts and call the create_posts function to create the posts
# PARAMETERS: The Width and Height for the window, the length of the base of the posts, the width and height of each post(which is the same), and the spacing between the posts.
# RETURN: NONE
def Hanoi_create(WIN_W, WIN_H, BASE, POST_W, POST_H, POST_SP):
    global btn_Quit
    global btn_Reset
    global msg_main
    
    #Creates the buttons
    btn_Quit = button_create(win, 10 , 20 , 70 , 30 , 'QUIT')   # returns a rect object
    btn_Reset = button_create(win, WIN_W-70-10, 20 , 70, 30 , 'RESET') # returns a rect object  

    global N_entry
    
    #Creates the entry 
    # [text of the getText, the message object displayed, The entry object]
    N_entry = [msg_main.getText(), msg_main, None]
    
    N_entry = [3 , msg_main, None]
    
    N_entry[2] = Entry(Point(WIN_W-35-10, 70), 1) # Defines the 2nd index as the entry object
    N_entry[2].setFill('white')
    N_entry[2].draw(win)
    
#    N_entry[1].setText(str(N_entry[0])) # Displays whatever is stored in the object msg_main
    
    
    Text(Point(WIN_W-50-10 , 70), 'N:').draw(win) # The text beside the entry textbox
    

    
    #Creates the BASE line
    line = Line(Point(0, WIN_H-BASE), Point(WIN_W, WIN_H-BASE))
    line.draw(win)
    
    #Creates the posts
    create_posts(WIN_W, WIN_H, BASE, POST_W, POST_H, POST_SP)    


    Hanoi_reset(POST_SP, BASE, WIN_W, WIN_H)


#PURPOSE: Determines that if the 2nd click which the user makes is on a post or not
#PARAMETERS: A string containing the name of the post where the first click has been made
#RETURN: A tuple containing the post names (first click-> src,   second click) if the 2nd click is a post
#        OR returns None if the 2nd click is not on a post
def wait_move(src):
    
    global text_2
    global click_count

    
    pt = win.getMouse()  #2nd mouse click
    
    
    # To track the second mouse click 
    click_count+=1 
    text_2.setText('Mouse Clicked: '+ str(click_count))
    
    
    if in_Rectangle(pt, posts[0][1]):   #2nd click on post A
        if src == posts[0][0]: # If the 
            msg_main.setText('NO MOVE ')
            return None                   
        else:
            msg_main.setText('MOVE ' + src + ' to ' + posts[0][0] )     
            return (posts[ord(src)-ord('A')] , posts[0])

    elif in_Rectangle(pt, posts[1][1]): #2nd click on post B
        if src == posts[1][0]: 
            msg_main.setText('NO MOVE ')
            return None        
        else:
            msg_main.setText('MOVE ' + src + ' to ' + posts[1][0])
            return (posts[ord(src)-ord('A')] , posts[1])

    elif in_Rectangle(pt, posts[2][1]): #2nd click on post C
        if src == posts[2][0]: 
            msg_main.setText('NO MOVE ')
            return None
        else:
            msg_main.setText('MOVE ' + src + ' to ' + posts[2][0])
            return (posts[ord(src)-ord('A')] , posts[2])


    else: # If the 2nd mouse click is not on a post 
        msg_main.setText("Coordinates are: "+ str((pt.x, pt.y)))
        return None
    



#PURPOSE: When the mouse is clicked inside a post, then this function changes the text and changes
#         the color of the post with a time lag
#PARAMETERS: The list of just that post where the mouse has been first clicked
#RETURN: A tuple containing the list of the specific post where mouse is first clicked 
#        OR returns None when the either of the click is outside any of the posts
#     post = [name -> A,B,C, Rectangle(), Text()-> object of text, disklist]
def process_post(post):
    
    msg_main.setText('POST: ' + post[0])  
    
    return_value = wait_move(post[0])
    if return_value == None:
        post[1].setFill('red')
        sleep(0.5)        
        post[1].setFill('brown')
    
    else:
        post[1].setFill('green')
        sleep(0.5)        
        post[1].setFill('brown')        
  
    return return_value 



#PURPOSE: Checks whether the disk clicked the top disk or not. If yes, then it calls the function wait_move() to get the 2nd Mouse click 
#         to determine as to where is the mouse clicked for the second time 
#PARAMETERS: The list of the disk which has been clicked by the user
#RETURN: If the disk which is clicked is the top one, then the function returns the set of tuple or None value as returned by the wait_move() function
#        Else the user click is not on the top disk, the function returns None

def process_disk(disk):
    msg_main.setText('DISK: ' + disk[0]+ '\nPOST: '+ disk[1] )
    
    if int(disk[0]) == posts[ord(disk[1])- ord('A')]  [3]  [-1]: # If the id of the disk is equal to the last value in the disklist of that post
        # Explaination:   [ord('C')-ord('A')] -> gives the index of the post
        #                 [3]                 -> gives us the disklist
        #                 [-1]                -> gives us the last element in the disklist
        disk[2].setFill('green')
        sleep(0.5)
        disk[2].setFill('yellow')
        
        return_value = wait_move(disk[1])
        return return_value        
        
            
    else:     
        msg_main.setText('NO MOVE')
        disk[2].setFill('red')
        sleep(0.5)
        disk[2].setFill('yellow')
        return None 
    
    
    
#PURPOSE: This function moves the top disk from one post to the other 
#PARAMETERS: Recieves the post from where the disk has to be popped and the destination of the post where the disk has to be appended
#RETURN: NONE

def Hanoi_move(src, dest):
    # disks =  [ [ disk_id, post_name, Rectangle, Text ], ... ]
    #           [ [ n-i ,    'A'      , Rect,     Text to display disk id]] 
    
    # [name -> A,B,C, Rectangle(), Text()-> object of text, disklist]
    
    
    if src[3] == []: #As it is not possible to pop out anything from the disklist if the disklist is empty
        msg_main.setText('NO MOVE')
        return None #Just returns back to the GUI loop 
    
    dest[3].append(src[3].pop()) #The disklist is modified when a disk moves from one post to the other  
    show_post_info() #The changes in the text objects for each of the disklists under each of the posts are shown
    
    for disk in disks:
        if int(disk[0]) == dest[3][-1]:  # If the id of the disk is equal t--o the id which has just been added to the disklist
            
            disk[1] = dest[0] #The post name under the disk is modified
            disk[2].undraw() # Undraws the rectangle as now it has to be moved
            disk[3].undraw() # Undraws the text as now it has to be moved
            
            w = disk[2].getP2().x - disk[2].getP1().x #Width of the disk
            h = disk[2].getP2().y - disk[2].getP1().y #height of the disk
                    
            x, y = (dest[1].getP1().x + dest[1].getP2().x )//2 ,  dest[1].getP2().y 
            # x = the position where the centre of the post lies
            # y = the position where the bottom of the post lies (the y2 coordinate)
            disk[2] = Rectangle(Point(x - w//2, (y-h*(len(dest[3])))), Point(x+w//2, y-h*(len(dest[3])-1)))  #Redefining the rectangle with new co-ordinates
            disk[2].setFill('yellow')
            disk[2].draw(win)
            
            disk[3] = Text((Point((disk[2].getP1().x + disk[2].getP2().x)//2, (disk[2].getP1().y + disk[2].getP2().y)//2)) , disk[0] )#Redefining the text with new co-ordinates
            disk[3].draw(win)
            
#PURPOSE: It detects if the disk from the source post is greater than the top disk at the destination post. 
#         If it is greater, then don't move the disks(Return False) 
#         and if the source disk is smaller than the top disk, then to move them, return True

#PARAMETERS: The source post object, the destination post object
#RETURN: True if the move is valide,     False if the move is invalid 
def Hanoi_rules(src, dest):
    
    # Post -   [name -> A,B,C, Rectangle(), Text()-> object of text, disklist]
    # Disks =  [ [ disk_id, post_name, Rectangle, Text ], ... ]   
     
    if src[3]== [] or dest[3] == []: #If the any of the posts are empty ie. without any disks
        return True  
    
    elif src[3][-1] < dest[3][-1]: # If the last element of the disklist of the source is greater than the last element of the disklist of the destination 
        return True
    
    else:   
        msg_main.setText('NO MOVE')

        #As the disk is created in the descending order like [3, 2, 1], i.e the biggest one was the first one, so using len(disks)- ...       
        disks[len(disks)- src[3][-1]  ][2].setFill('red')           
        sleep(0.5)
        disks[len(disks)- src[3][-1]  ][2].setFill('yellow')
        return False


# PURPOSE: The main function which performs everything by calling every other function for their respective purpose. It engages in a GUI loop to get the mouse click by the user 
#           and performs a specific function according to the coordinates of the place where the mouse is clicked 
# PARAMETERS: NONE
# RETURN: NONE    
def main():
    WIN_W, WIN_H = 500, 400
    BASE, POST_W, POST_H, POST_SP = 100, 15, 150, WIN_W//4
    
    global win
    global msg_main
    global text_2  #For displaying the text for Mouse Clicks [BONUS]
    global click_count   #To keep track of Mouse Clicks by clicking on the objects [BONUS]


    
    win = GraphWin("Hanoi Towers", WIN_W, WIN_H)
    msg_main = Text(Point(WIN_W//2, 20), "GREETINGS!")
    msg_main.draw(win)  
    
    #[Bonus] Text for displaying how many times the mouse has been clicked 
    click_count = 0
    text_2 = Text(Point(WIN_W//2, 50), 'Mouse Clicked: '+ str(click_count))
    text_2.draw(win)     
    
    #[BONUS] Text for displaying PERFECT!
    perfect = Text (Point(WIN_W//2, 80), '')
    perfect.setFill('red')
             
    Hanoi_create(WIN_W, WIN_H, BASE, POST_W, POST_H, POST_SP)
    
    move_count = 0 # To count the number of moves
    
    while True:        
        pt = win.getMouse()
        click_count+=1    
        text_2.setText('Mouse Clicked: '+ str(click_count))        
        
        try:
         
            if in_Rectangle(pt, btn_Quit): # Quit Button
                msg_main.setText('BYE BYE!') 
                win.getMouse()
                break
            
            elif in_Rectangle(pt, btn_Reset): # Reset button
                Hanoi_reset(POST_SP, BASE, WIN_W, WIN_H)
                move_count = 0
                click_count = 0
                text_2.setText('Mouse Clicked: '+ str(click_count))        
                
            
            #If the value of clicked is not changed in the loop, then the statement after the for loop is also not executed
            clicked = False
            
            for i in range(len(disks)): # SCANS through the disks
                if in_Rectangle(pt, disks[i][2]):  #If the point is found in that particular disk
                    returned_val =  process_disk(disks[i])
                    # if both the clicks are valid,       returned_val = (src, dest) 
                    # if any of the clicks are invalid,   returned val == None
                    
                    if returned_val == None: #If the returned_val = None; which means that there was an invalid click
                        continue            #Go back to the beginning of the GUI loop
                    else:
                        src, dest = returned_val 
                        if Hanoi_rules(src, dest): #If the conditions are met, then move the objects
                            Hanoi_move(src, dest)
                            move_count += 1
                            clicked = True
                            break  # Break out of the for loop
                        
                        else:
                            continue         
            
            #When the control comes out of the for loop, and the move has been made, then continue(Not to execute anything else like the Coordinates display)
            if clicked == True:  continue        
            
                                               
            elif in_Rectangle(pt, posts[0][1]): # Post A
                returned_val =  process_post(posts[0])
                # if both the clicks are valid,       returned_val = (src, dest) 
                # if any of the clicks are invalid,   returned val == None
                
                if returned_val == None: #If the returned_val = None; which means that there was an invalid click
                    continue
                else:
                    src, dest = returned_val                 
                    if Hanoi_rules(src, dest): #If the conditions are met, then move the objects
                        Hanoi_move(src, dest)
                        move_count += 1
                    else:
                        continue         
    
                    
            elif in_Rectangle(pt, posts[1][1]): #Post B
                returned_val =  process_post(posts[1])
                # if both the clicks are valid,       returned_val = (src, dest) 
                # if any of the clicks are invalid,   returned val == None
                
                if returned_val == None: #If the returned_val = None; which means that there was an invalid click
                    continue
                else:
                    src, dest = returned_val                 
                    if Hanoi_rules(src, dest): #If the conditions are met, then move the objects
                        Hanoi_move(src, dest)
                        move_count += 1
                    else:
                        continue         
                    
            
            elif in_Rectangle(pt, posts[2][1]): # Post C
                returned_val =  process_post(posts[2])
                # if both the clicks are valid,       returned_val = (src, dest) 
                # if any of the clicks are invalid,   returned val == None
                
                if returned_val == None: #If the returned_val = None; which means that there was an invalid click
                    continue
                else:
                    src, dest = returned_val 
                    if Hanoi_rules(src, dest): #If the conditions are met, then move the objects
                        Hanoi_move(src, dest)
                        move_count += 1
                        
                    else:
                        continue                         
            
            
            else:
                msg_main.setText("Coordinates are: "+ str((pt.x, pt.y)))
    
    
            if len(posts[2][3]) == len(disks) and posts[0][3] == [] and posts[1][3] == [] :  #and move_count== (2** len(disks)) -1
                msg_main.setText('CONGRATULATIONS !!')
                msg_main.setFill('red')
                    
                for i in range(5):
                    sleep(0.3)
                    perfect.draw(win)
                    perfect.setText('PERFECT!!')
                    sleep(0.3)
                    perfect.undraw()
                
                win.getMouse()
                break
        
        except:
            print("Invalid point")
    
    win.close()
    
    
main()
