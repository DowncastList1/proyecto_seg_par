/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package common;

import java.awt.Color;

/**
 *
 * @author angel
 */
public class Constants {
    public static int CARD_X_SIZE = 100;
    public static int CARD_Y_SIZE = 160;
    
    public static int WINDOW_X_SIZE = 1500;
    public static int WINDOW_Y_SIZE = 800;
    
    public static Color groupsColor = new Color(80, 90, 70, 150);
    public static Color backGroundColor = new Color(51, 161, 73);
    public static Color selectedCardColor = new Color(227, 98, 106, 100);
    
    public static int SPACE_BETWEEN_CARDS_IN_LIST = 30;
    public static int SPACE_BETWEEN_GROUPS = 150;
    public static int MENU_MIN_LENGT = 40;
    public static int MENU_MAX_LENGT = 200;
    
    public static class Sounds {
    	public static String CARD_OK = "button-click.wav";
    	public static String STROKE = "carton-impact-5.wav";
    	public static String DRAGGING = "smokearrodillandose-001.wav";
    	public static String CLICK_PROVIDER = "sinnett-card.wav";
        public static String MENU_CHANGE = "menu_change.wav";
        public static String MIX_DECK = "mix_deck.wav";
    }

}
