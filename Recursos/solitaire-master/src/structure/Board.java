/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package structure;

import common.Utils;
import common.Constants;
import java.awt.Graphics;
import java.awt.image.ImageObserver;
import java.util.LinkedList;

/**
 *
 * @author angel
 */
public class Board{
    
    private int x_clicket_in_dragged_card;
    private int y_clicket_in_dragged_card;
    private final CardsGroup draggedCards;
    private CardsGroup groupOwnerOfDraggedCards;

    private final CardsGroup provider1;
    private final CardsGroup provider2;
    
    private final CardsGroup groupCompleted1;
    private final CardsGroup groupCompleted2;
    private final CardsGroup groupCompleted3;
    private final CardsGroup groupCompleted4;
    
    private final CardsGroup gameGroup1;
    private final CardsGroup gameGroup2;
    private final CardsGroup gameGroup3;
    private final CardsGroup gameGroup4;
    private final CardsGroup gameGroup5;
    private final CardsGroup gameGroup6;
    private final CardsGroup gameGroup7;
    
    private final Utils sound;
    
    public Board(){
        draggedCards = new CardsGroup(0, 0, 0, 0, 13, "vertical");

        provider1 = new CardsGroup(100, 20, 0, -1, 0, "onTop");
        provider2 = new CardsGroup(300, 20, 0, -2, 1, "horizontal");
        
        groupCompleted1 = new CardsGroup(700, 20, 0, -3, 1, "onTop");
        groupCompleted2 = new CardsGroup(900, 20, 0, -4, 1, "onTop");
        groupCompleted3 = new CardsGroup(1100, 20, 0, -5, 1, "onTop");
        groupCompleted4 = new CardsGroup(1300, 20, 0, -6, 1, "onTop");
        
        gameGroup1 = new CardsGroup(100, 400, 1, 1, 13, "vertical");
        gameGroup2 = new CardsGroup(300, 400, 2, 2, 13, "vertical");
        gameGroup3 = new CardsGroup(500, 400, 3, 3, 13, "vertical");
        gameGroup4 = new CardsGroup(700, 400, 4, 4, 13, "vertical");
        gameGroup5 = new CardsGroup(900, 400, 5, 5, 13, "vertical");
        gameGroup6 = new CardsGroup(1100, 400, 6, 6, 13, "vertical");
        gameGroup7 = new CardsGroup(1300, 400, 7, 7, 13, "vertical");
        
        sound = new Utils();
    }
    
    public void drawBoard(Graphics g, ImageObserver observer){
        g.setColor(Constants.groupsColor);

        g.fillRect(provider1.getX_position(), provider1.getY_position(), provider1.getX_size(), provider1.getY_size());
        g.fillRect(provider2.getX_position(), provider2.getY_position(), provider2.getX_size(), provider2.getY_size());
        
        g.fillRect(groupCompleted1.getX_position(), groupCompleted1.getY_position(), groupCompleted1.getX_size(), groupCompleted1.getY_size());
        g.fillRect(groupCompleted2.getX_position(), groupCompleted2.getY_position(), groupCompleted2.getX_size(), groupCompleted2.getY_size());
        g.fillRect(groupCompleted3.getX_position(), groupCompleted3.getY_position(), groupCompleted3.getX_size(), groupCompleted3.getY_size());
        g.fillRect(groupCompleted4.getX_position(), groupCompleted4.getY_position(), groupCompleted4.getX_size(), groupCompleted4.getY_size());
        
        g.fillRect(gameGroup1.getX_position(), gameGroup1.getY_position(), gameGroup1.getX_size(), gameGroup1.getY_size());
        g.fillRect(gameGroup2.getX_position(), gameGroup2.getY_position(), gameGroup2.getX_size(), gameGroup2.getY_size());
        g.fillRect(gameGroup3.getX_position(), gameGroup3.getY_position(), gameGroup3.getX_size(), gameGroup3.getY_size());
        g.fillRect(gameGroup4.getX_position(), gameGroup4.getY_position(), gameGroup4.getX_size(), gameGroup4.getY_size());        
        g.fillRect(gameGroup5.getX_position(), gameGroup5.getY_position(), gameGroup5.getX_size(), gameGroup5.getY_size());
        g.fillRect(gameGroup6.getX_position(), gameGroup6.getY_position(), gameGroup6.getX_size(), gameGroup6.getY_size());
        g.fillRect(gameGroup7.getX_position(), gameGroup7.getY_position(), gameGroup7.getX_size(), gameGroup7.getY_size());
        
        this.drawCards(provider1.getCards(), g, observer);
        this.drawCards(provider2.getCards(), g, observer);
        
        this.drawCards(groupCompleted1.getCards(), g, observer);
        this.drawCards(groupCompleted2.getCards(), g, observer);
        this.drawCards(groupCompleted3.getCards(), g, observer);
        this.drawCards(groupCompleted4.getCards(), g, observer);
        
        this.drawCards(gameGroup1.getCards(), g, observer);
        this.drawCards(gameGroup2.getCards(), g, observer);
        this.drawCards(gameGroup3.getCards(), g, observer);
        this.drawCards(gameGroup4.getCards(), g, observer);
        this.drawCards(gameGroup5.getCards(), g, observer);
        this.drawCards(gameGroup6.getCards(), g, observer);
        this.drawCards(gameGroup7.getCards(), g, observer);
        
        // dragged cards should be draw at the end
        this.drawDraggedCards(draggedCards.getCards(), g, observer);
    }
    
    private void drawCards(LinkedList<Card> cards, Graphics g, ImageObserver observer){
        Card card;
        for (int i = 0; i < cards.size(); i++) {
            card = cards.get(i);
            // If the card is visible, show the card
            if(card.isVisible()){
                g.drawImage(card.getImage(), card.getImageXLocation(), card.getImageYLocation(), 
                        card.getImageXSize(), card.getImageYSize(), observer);
            }else{
                // If the card is hidden, show the image that represents a card not available
                g.drawImage(Deck.HIDDEN_SIDE, card.getImageXLocation(), card.getImageYLocation(), 
                        card.getImageXSize(), card.getImageYSize(), observer);
            }
        }
    }

    private void drawDraggedCards(LinkedList<Card> cards, Graphics g, ImageObserver observer){
        Card card;
        Card initial = cards.size() > 0 ? cards.get(0) : new Card();

        g.setColor(Constants.selectedCardColor);
        for (int i = 0; i < cards.size(); i++) {
            card = cards.get(i);

            g.drawImage(card.getImage(), initial.getImageXLocation(), initial.getImageYLocation() + i * Constants.SPACE_BETWEEN_CARDS_IN_LIST, 
                    card.getImageXSize(), card.getImageYSize(), observer);
            g.fillRect(initial.getImageXLocation(), initial.getImageYLocation() + i * Constants.SPACE_BETWEEN_CARDS_IN_LIST, card.getImageXSize(), card.getImageYSize());
        }
    }
    
    // This method is used to add the cards to each group when the game starts
    public void addCards(LinkedList<Card> cards){
        int currentStack = 1;
        Card currentCard;

        while(cards.size() > 0) {
            switch(currentStack){
                case 1:
                    currentStack = setInitialCardData(cards, gameGroup1, currentStack);
                    break;
                case 2:
                    currentStack = setInitialCardData(cards, gameGroup2, currentStack);
                    break;
                case 3:
                    currentStack = setInitialCardData(cards, gameGroup3, currentStack);
                    break;
                case 4:
                    currentStack = setInitialCardData(cards, gameGroup4, currentStack);
                    break;
                case 5:
                    currentStack = setInitialCardData(cards, gameGroup5, currentStack);
                    break;
                case 6:
                    currentStack = setInitialCardData(cards, gameGroup6, currentStack);
                    break;
                case 7:
                    currentStack = setInitialCardData(cards, gameGroup7, currentStack);
                    break;
                case 8:
                    currentCard = cards.remove();
                    currentCard.setIsVisible(false);
                    currentCard.setImageXLocation(provider1.getX_position());
                    currentCard.setImageYLocation(provider1.getY_position());
                    provider1.addCard(currentCard);
                    break;
            }
        }
    }
    
    /**
     * This define the initial state of the cards in the 7 play groups, n cards hidden and the last one should be visible
     * @param cards
     * @param cardGroup
     * @param currentStack
     * @return 
     */
    private int setInitialCardData(LinkedList<Card> cards, CardsGroup cardGroup, int currentStack){
        Card currentCard;
        // When the last card is going to be added, then make card visible
        currentCard = cards.remove();
        currentCard.setImageXLocation(cardGroup.getX_position());
        currentCard.setImageYLocation(cardGroup.getY_position() + cardGroup.getCards().size() * Constants.SPACE_BETWEEN_CARDS_IN_LIST);
        if(cardGroup.getCards().size() + 1 == cardGroup.getLimit()){

            currentCard.setIsVisible(true);
            cardGroup.addCard(currentCard);
            currentStack++;
        }else{
            // Add the card hidden

            currentCard.setIsVisible(false);
            cardGroup.addCard(currentCard);
        }
        return currentStack;
    }
    
    public void clickProvider(int x, int y){
    	
        // When provider list 1 is clicked
        if(this.isXYInsideXYRegion(x, y, this.provider1.getX_position(), this.provider1.getY_position())){
            Card card = null;
            
            if(provider1.getCards().isEmpty() && provider2.getCards().isEmpty()){
                return;
            }
            sound.playSound(Constants.Sounds.CLICK_PROVIDER);

            // TODO: Fix this issue, first card needs to be shown in this order, 123(1) 456(itr 2) remove 6, next itr swow543 
            while(!provider2.getCards().isEmpty()){
                card = provider2.getCards().removeFirst();
                card.setImageXLocation(provider1.getX_position());
                card.setImageYLocation(provider1.getY_position());
                card.setIsVisible(false);

                provider1.getCards().addLast(card);
            }
            System.out.println(card != null? x-card.getImageXLocation(): -1);
            System.out.println(card != null? y-card.getImageYLocation(): -1);

            // move three or less cards to provider 2
            for (int i = 0; i < 3; i++) {
                if(provider1.getCards().size() > 0){
                    
                    card = provider1.getCards().remove();
                    card.setImageXLocation(provider2.getX_position() + i * Constants.SPACE_BETWEEN_CARDS_IN_LIST);
                    card.setImageYLocation(provider2.getY_position());
                    card.setIsVisible(true);

                    provider2.addCard(card);
                }
            }
        }
    }
    
    public void draggImages(int x, int y){
        // When the list draggedCards contains cards, dont search for new cards to dragg only update coordinates
        if(!draggedCards.getCards().isEmpty()){
            Card card = draggedCards.getCards().get(0);

            card.setImageXLocation(x - x_clicket_in_dragged_card);
            card.setImageYLocation(y - y_clicket_in_dragged_card);
        }else{
            // If not dragging cards, search if the received coordinates are inside a group
            this.searchImageInList(x, y, groupCompleted1);
            this.searchImageInList(x, y, groupCompleted2);
            this.searchImageInList(x, y, groupCompleted3);
            this.searchImageInList(x, y, groupCompleted4);
            
            this.searchImageInList(x, y, gameGroup1);
            this.searchImageInList(x, y, gameGroup2);
            this.searchImageInList(x, y, gameGroup3);
            this.searchImageInList(x, y, gameGroup4);
            this.searchImageInList(x, y, gameGroup5);
            this.searchImageInList(x, y, gameGroup6);
            this.searchImageInList(x, y, gameGroup7);
            
            this.searchImageInList(x, y, provider2);
        }
    }

    private void searchImageInList(int x, int y, CardsGroup cards){
        Card card;

        for (int i = cards.getCards().size() -1; i > -1; i--) {
            card = cards.getCards().get(i);

            // If we are dragging inside one card add cards to draggedCards list
            if(this.isXYInsideXYRegion(x, y, card.getImageXLocation(), card.getImageYLocation())){
                
                // If card not visible or if we are trying to drag more cards than allowed in one group
                if (!card.isVisible() || cards.getCards().size() - i > cards.getDraggedCardsAllowed()) {
                    return;
                }
                
                // This is to calculate how many units needs to be substracted to the card in order to 
                // draw it in the same way we clicked
                // if we disable this, the mouse will be in the 0, 0 (top left corner) of the card
                this.x_clicket_in_dragged_card = x - card.getImageXLocation();
                this.y_clicket_in_dragged_card = y - card.getImageYLocation();
                
                sound.playSound(Constants.Sounds.DRAGGING);
                // Add the card, and the cards next to that one into draggedCards list
                int cardsSize = cards.getCards().size();
                for (int j = i; j < cardsSize; j++) {
                    card = cards.getCards().remove(i);
                    card.setIsSelected(true);
                    card.setImageXLocation(x - this.x_clicket_in_dragged_card);
                    card.setImageYLocation(y - this.y_clicket_in_dragged_card + draggedCards.getCards().size() * Constants.SPACE_BETWEEN_CARDS_IN_LIST);
                    draggedCards.getCards().add(card);
                }
                
                // Update the group owner, this will be used as a reference to the group that contains
                // the cards before dragging and latter, we can use this reference in order to return the cards to original list
                this.groupOwnerOfDraggedCards = cards;

                return;
            }
        }
    }
    
    public void releaseCards(int x, int y){
        // Verify if we release the cards inside one group coordinates
        if(!draggedCards.getCards().isEmpty()){
            if(this.isXYInsideXYRegion(x, y, 
                    this.gameGroup1.getX_position(), 
                    this.gameGroup1.getY_position() + (this.gameGroup1.getCards().size() -1)  * Constants.SPACE_BETWEEN_CARDS_IN_LIST)){

                conditionsForGameGroups(gameGroup1, draggedCards);
            }else if(this.isXYInsideXYRegion(x, y, 
                    this.gameGroup2.getX_position(),
                    this.gameGroup2.getY_position() + (this.gameGroup2.getCards().size() -1)  * Constants.SPACE_BETWEEN_CARDS_IN_LIST)){

                conditionsForGameGroups(gameGroup2, draggedCards);
            }else if(this.isXYInsideXYRegion(x, y, 
                    this.gameGroup3.getX_position(),
                    this.gameGroup3.getY_position() + (this.gameGroup3.getCards().size() -1)  * Constants.SPACE_BETWEEN_CARDS_IN_LIST)){
                
                conditionsForGameGroups(gameGroup3, draggedCards);
            }else if(this.isXYInsideXYRegion(x, y, 
                    this.gameGroup4.getX_position(),
                    this.gameGroup4.getY_position() + (this.gameGroup4.getCards().size() -1)  * Constants.SPACE_BETWEEN_CARDS_IN_LIST)){
                
                conditionsForGameGroups(gameGroup4, draggedCards);
            }else if(this.isXYInsideXYRegion(x, y, 
                    this.gameGroup5.getX_position(), 
                    this.gameGroup5.getY_position() + (this.gameGroup5.getCards().size() -1) * Constants.SPACE_BETWEEN_CARDS_IN_LIST)){
                
               conditionsForGameGroups(gameGroup5, draggedCards);
            }else if(this.isXYInsideXYRegion(x, y, 
                    this.gameGroup6.getX_position(), 
                    this.gameGroup6.getY_position() + (this.gameGroup6.getCards().size() -1) * Constants.SPACE_BETWEEN_CARDS_IN_LIST)){
                
                conditionsForGameGroups(gameGroup6, draggedCards);
            }else if(this.isXYInsideXYRegion(x, y, 
                    this.gameGroup7.getX_position(), 
                    this.gameGroup7.getY_position() + (this.gameGroup7.getCards().size() -1) * Constants.SPACE_BETWEEN_CARDS_IN_LIST)){
                
                conditionsForGameGroups(gameGroup7, draggedCards);
            }else if(this.isXYInsideXYRegion(x, y, this.groupCompleted1.getX_position(), this.groupCompleted1.getY_position())){
                
                 conditionsForGroupsCompleted(groupCompleted1, draggedCards);
             }else if(this.isXYInsideXYRegion(x, y, this.groupCompleted2.getX_position(), this.groupCompleted2.getY_position())){
                 
                 conditionsForGroupsCompleted(groupCompleted2, draggedCards);
             }else if(this.isXYInsideXYRegion(x, y, this.groupCompleted3.getX_position(), this.groupCompleted3.getY_position())){
                 
                 conditionsForGroupsCompleted(groupCompleted3, draggedCards);
             }else if(this.isXYInsideXYRegion(x, y, this.groupCompleted4.getX_position(), this.groupCompleted4.getY_position())){
                 
                 conditionsForGroupsCompleted(groupCompleted4, draggedCards);
             }else{
                this.moveAllCardsToAnotherList(draggedCards, groupOwnerOfDraggedCards);
                sound.playSound(Constants.Sounds.STROKE);
             }
        }
    }

    private void conditionsForGroupsCompleted(CardsGroup group, CardsGroup draggedCards){
        
        if(draggedCards.getCards().size() == 1){
            // When trying to add a card to the same group that had the card before
            if (group.getId() == groupOwnerOfDraggedCards.getId()) {
                moveAllCardsToAnotherList(draggedCards, groupOwnerOfDraggedCards);
                return;
            }
            Card draggedCard = draggedCards.getCards().getFirst();

            if(group.getCards().size() > 0 && 
                    group.getCards().getLast().getNumber()+1 == draggedCard.getNumber() && 
                    group.getCards().getLast().getGroup() == draggedCard.getGroup()){

                group.addCard(draggedCard);
                draggedCard.setIsSelected(false);
                draggedCards.getCards().remove();
                sound.playSound(Constants.Sounds.CARD_OK);
                this.setNewCoordinates(draggedCard, group);
                if(groupOwnerOfDraggedCards.getCards().size() > 0 && !groupOwnerOfDraggedCards.getCards().getFirst().isVisible()){
                    groupOwnerOfDraggedCards.getCards().getLast().setIsVisible(true);
                }
            }else if(group.getCards().isEmpty() && draggedCard.getNumber() == 1){

                group.addCard(draggedCard);
                draggedCard.setIsSelected(false);
                draggedCards.getCards().remove();
                this.setNewCoordinates(draggedCard, group);
                sound.playSound(Constants.Sounds.CARD_OK);
                if(groupOwnerOfDraggedCards.getCards().size() > 0 && !groupOwnerOfDraggedCards.getCards().getFirst().isVisible()){
                    groupOwnerOfDraggedCards.getCards().getLast().setIsVisible(true);
                }
            }else{
                this.setNewCoordinates(draggedCard, groupOwnerOfDraggedCards);
                groupOwnerOfDraggedCards.addCard(draggedCard);
                draggedCard.setIsSelected(false);
                draggedCards.getCards().remove();
                sound.playSound(Constants.Sounds.STROKE);
            }
        }else{
            this.moveAllCardsToAnotherList(draggedCards, groupOwnerOfDraggedCards);
        }
    }
    
    private void conditionsForGameGroups(CardsGroup group, CardsGroup draggedCards){
            Card draggedCard = draggedCards.getCards().getFirst();
            
            // When trying to add a card to the same group that had the card before
            if (group.getId() == groupOwnerOfDraggedCards.getId()) {
                moveAllCardsToAnotherList(draggedCards, groupOwnerOfDraggedCards);
                return;
            }
            if(group.getCards().size() > 0 && 
                    group.getCards().getLast().getNumber()-1 == draggedCard.getNumber() && 
                    group.getCards().getLast().isRedColor() != draggedCards.getCards().getFirst().isRedColor()){

                this.moveAllCardsToAnotherList(draggedCards, group);
                sound.playSound(Constants.Sounds.CARD_OK);
                if(groupOwnerOfDraggedCards.getCards().size() > 0 && !groupOwnerOfDraggedCards.getCards().getFirst().isVisible()){
                    groupOwnerOfDraggedCards.getCards().getLast().setIsVisible(true);
                }
            }else if(group.getCards().isEmpty() && draggedCard.getNumber() == 13){
                this.moveAllCardsToAnotherList(draggedCards, group);
                sound.playSound(Constants.Sounds.CARD_OK);
                if(groupOwnerOfDraggedCards.getCards().size() > 0 && !groupOwnerOfDraggedCards.getCards().getFirst().isVisible()){
                    groupOwnerOfDraggedCards.getCards().getLast().setIsVisible(true);
                }
            }else{
                moveAllCardsToAnotherList(draggedCards, groupOwnerOfDraggedCards);
            }
    }

    private boolean isXYInsideXYRegion(int mouse_x, int mouse_y, int region_x, int region_y){
        if(mouse_x >= region_x && mouse_x <= region_x + Constants.CARD_X_SIZE
            && mouse_y >= region_y  && mouse_y <= region_y + Constants.CARD_Y_SIZE){
            return true;
        }
        return false;
    }

    private void moveAllCardsToAnotherList(CardsGroup source, CardsGroup target){
        Card card;
        while(!source.getCards().isEmpty()){
            card = source.getCards().remove();
            card.setIsSelected(false);
            this.setNewCoordinates(card, target);
            target.addCard(card);
        }
        sound.playSound(Constants.Sounds.STROKE);
        
    }
    private void setNewCoordinates(Card card, CardsGroup groupOwner){
        switch(groupOwner.getOrderType()){
            case "onTop":
                card.setImageXLocation(groupOwner.getX_position());
                card.setImageYLocation(groupOwner.getY_position());
                break;
            case "vertical":
                card.setImageXLocation(groupOwner.getX_position());
                card.setImageYLocation(groupOwner.getY_position() + groupOwner.getCards().size() * Constants.SPACE_BETWEEN_CARDS_IN_LIST);
                break;
            case "horizontal":
                card.setImageXLocation(groupOwner.getX_position() + groupOwner.getCards().size() * Constants.SPACE_BETWEEN_CARDS_IN_LIST);
                card.setImageYLocation(groupOwner.getY_position());
                break;
        }
    }
}
