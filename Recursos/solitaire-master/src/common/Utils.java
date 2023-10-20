/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package common;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
/**
 *
 * @author angel
 */
public class Utils {
    
    public static void playSound(String soundName) {
    String gongFile = "res/sound/" + soundName;
	    try
	    {
	        Clip clip = AudioSystem.getClip();
	        clip.open(AudioSystem.getAudioInputStream(new File(gongFile)));
	        clip.start();
	    }
	    catch (Exception exc)
	    {
	        exc.printStackTrace(System.out);
	    }
    }
    
    public static BufferedImage readImage(String path){
        try {
           return ImageIO.read(new File("res/img/"+path));
        } catch (IOException e) {
        }
        return null;
    }
}
