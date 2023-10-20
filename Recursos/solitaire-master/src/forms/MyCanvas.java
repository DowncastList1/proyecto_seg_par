/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package forms;

import common.Constants;
import common.Utils;
import java.awt.Graphics;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionListener;
import javax.swing.JPanel;
import java.awt.event.MouseListener;
import structure.Board;
import structure.Deck;
import structure.Menu;

/**
 *
 * @author angel
 */
public class MyCanvas extends JPanel implements  MouseMotionListener, MouseListener{

    private Board board = new Board();
    private final Deck deck = new Deck();
    private final Menu menu = new Menu();
    
    public MyCanvas(){

        this.addMouseMotionListener(this);
        this.addMouseListener(this);
        
        board.addCards(deck.getCards());
    }
    
    @Override
    public void paint(Graphics g) {
        super.paint(g);
        
        g.setColor(Constants.backGroundColor);
        g.fillRect(0, 0, Constants.WINDOW_X_SIZE, Constants.WINDOW_Y_SIZE);
        
        board.drawBoard(g, this);
       
        menu.drawMenu(g);
    }

    @Override
    public void mouseDragged(MouseEvent me) {
        if (!menu.isIsActive()) {
            this.board.draggImages(me.getX(), me.getY());
        }else{
            menu.showHideMenu(this);
        }
        this.repaint();
    }

    @Override
    public void mouseMoved(MouseEvent me) {
    }

    @Override
    public void mouseClicked(MouseEvent me) {
        // If we click menu
        if(me.getX() <= menu.getSize()){
            if(menu.isIsActive()){
                this.validateMenuAnswer(this.menu.clickOption(me.getX(), me.getY(), this));
            }else{
                menu.showHideMenu(this);
                Utils.playSound(Constants.Sounds.MENU_CHANGE);
            }
        }
        if(!menu.isIsActive()){
            board.clickProvider(me.getX(), me.getY());
        }else{
            menu.showHideMenu(this);
        }
        
        repaint();
    }
    
    private void validateMenuAnswer(int response){
        switch(response){
            case 0:
                deck.newGame();
                board = new Board();
                board.addCards(deck.getCards());
                Utils.playSound(Constants.Sounds.MIX_DECK);
                repaint();
                break;
            default:
                Utils.playSound(Constants.Sounds.MENU_CHANGE);
                break;
        } 
    }

    @Override
    public void mousePressed(MouseEvent me) {
    }

    @Override
    public void mouseReleased(MouseEvent me) {
        if (!menu.isIsActive()) {
            this.board.releaseCards(me.getX(), me.getY());
        }
        this.repaint();
    }

    @Override
    public void mouseEntered(MouseEvent me) {
    }

    @Override
    public void mouseExited(MouseEvent me) {
    }
}
