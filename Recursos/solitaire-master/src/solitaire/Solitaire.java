/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package solitaire;

import common.Constants;
import forms.MainForm;
import forms.MyCanvas;
import java.awt.Color;

/**
 *
 * @author angel
 */
public class Solitaire {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        MainForm solitaire;
        
        // Define canvas components
        MyCanvas canvas = new MyCanvas();
        canvas.setSize(Constants.WINDOW_X_SIZE, Constants.WINDOW_Y_SIZE);
        canvas.setBackground(Color.yellow);
        
        // Add components and properties to main form
        solitaire = new MainForm();
        solitaire.pack();
        solitaire.setVisible(true);
        solitaire.setResizable(false);
        solitaire.setSize(Constants.WINDOW_X_SIZE, Constants.WINDOW_Y_SIZE);
        solitaire.add(canvas);
    }
    
}
