public class Pokemon {
protected int hp ;
public String cry ;
private String secret ;
private int power ;
public Pokemon () {
hp = 50;
cry = " Poke ? " ;
}
public Pokemon ( String c ) {
this (c , 50) ;
}
public Pokemon ( String c , int hp ) {
cry = c ;
this . hp = hp ;
}
public void attack ( Pokemon p ) {
p . hp -= power ;
}
public void talk () {
System . out . println ( cry ) ;
}
public void eat () {
System . out . println ( " nom nom " ) ;
}

public static void main(String[] args) {
	//Squirtle s = new Squirtle();
	//Pokemon z = new Pikachu();
	//s = (Squirtle) z;	
	Pokemon x = new Squirtle();
	Squirtle s = x;
}
}