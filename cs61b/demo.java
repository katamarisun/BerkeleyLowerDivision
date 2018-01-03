public static void foo(Superclass s){
  System.out.println("I am the super-est class!");
}

public static void foo(Subclass s){
  System.out.println("I'm not the super-est :(");
}

public static void main(String[] args) {
  Superclass s = new Subclass();
  Subclass s2 = s;

  foo(s);
  foo(s2);
}