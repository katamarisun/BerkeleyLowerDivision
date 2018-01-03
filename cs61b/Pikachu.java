public class Pikachu extends Pokemon {
public Pikachu () {
hp = 100;
}
public Pikachu (int hp ) {
super ( " Pika pika pikachu " , hp ) ;
}
public void attack ( Pokemon p ) {
p . hp = 0;
}
public void eat () {
System . out . println ( " nom Pika nom " ) ;
}
}