public class Main {
    public static void main(String[] args) {
        //Parte 1
        int resultadoSuma = suma(10, 20, 30);
        System.out.println(resultadoSuma);

        //Parte 2
        Coche coche = new Coche();
        coche.agregarPuerta();
        System.out.println(coche.numeroPuertas);
    }

    public static int suma(int a, int b, int c) {
        return a + b + c;
    }
}

