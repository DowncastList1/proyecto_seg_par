/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package structure;

import common.Constants;
import common.Utils;
import forms.MyCanvas;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author angel
 */
public class Menu implements Runnable{
    private int size;
    
    private MenuOption[] options;
    
    private boolean isActive;
    private MyCanvas myCanvas;
    public static final BufferedImage LEFT_ARROW = Utils.readImage("left_arrow.png");
    public static final BufferedImage RIGHT_ARROW = Utils.readImage("right_arrow.png");

    public Menu() {
        this.size = Constants.MENU_MIN_LENGT;
        this.isActive = false;
        
        options = new MenuOption[1];
        
        for (int i = 0; i < options.length; i++) {
            options[i] = new MenuOption(this.size - 200, 150 * (i + 1) + Constants.MENU_MIN_LENGT * i, 150, 150, i);
        }
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public MenuOption[] getOptions() {
        return options;
    }

    public void setOptions(MenuOption[] options) {
        this.options = options;
    }

    public boolean isIsActive() {
        return isActive;
    }

    public void setIsActive(boolean isActive) {
        this.isActive = isActive;
    }
    
    public void showHideMenu(MyCanvas my){
        myCanvas = my;
        new Thread(this).start();
    }
    
    public void drawMenu(Graphics g){
        g.setColor(Constants.groupsColor);
        
        g.fillRect(0, 0, this.getSize(), Constants.WINDOW_Y_SIZE);

        MenuOption option;
        for (int i = 0; i < options.length; i++) {
            option = options[i];
            g.drawImage(option.getImage(), this.size - option.getX_size() - Constants.MENU_MIN_LENGT, option.getY_size() * (i + 1) + Constants.MENU_MIN_LENGT * i, option.getX_size(), option.getY_size(), myCanvas);
        }
        if(this.isActive){
            g.drawImage(LEFT_ARROW, this.size - Constants.MENU_MIN_LENGT, 0, 40, 40, myCanvas);
        }else{
            g.drawImage(RIGHT_ARROW, this.size - Constants.MENU_MIN_LENGT, 0, 40, 40, myCanvas);
        }
    }
    
    public int clickOption(int x, int y, MyCanvas my){
        MenuOption option;
        for (int i = 0; i < options.length; i++) {
            option = options[i];
            if(x > this.size - option.getX_size() - Constants.MENU_MIN_LENGT && x < this.size - Constants.MENU_MIN_LENGT
                    && y > (option.getY_size() * (i + 1) + Constants.MENU_MIN_LENGT * i) && y < (option.getY_size() * (i + 1) + Constants.MENU_MIN_LENGT * i) + option.getY_size()){
                
                option.setIsActive(true);
                return i;
            }
        }
        this.showHideMenu(my);
        return -1;
    }

    @Override
    public void run() {
        if (!isActive) {
            while( this.size < Constants.MENU_MAX_LENGT) {
                this.size ++;
                myCanvas.repaint();
                try {
                    Thread.sleep(1l);
                } catch (InterruptedException ex) {
                    Logger.getLogger(Menu.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
            this.setIsActive(true);
        }else{
            while(this.size > Constants.MENU_MIN_LENGT){
                this.size --;
                myCanvas.repaint();

                try {
                    Thread.sleep(1l);
                } catch (InterruptedException ex) {
                    Logger.getLogger(Menu.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
            this.setIsActive(false);
        }
    }
    
}
