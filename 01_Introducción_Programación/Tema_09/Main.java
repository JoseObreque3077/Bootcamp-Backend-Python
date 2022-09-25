public class Main {
    public static void main(String[] args) {
        //Parte 1: cliente
        Cliente cliente = new Cliente();

        cliente.setNombre("Claudio");
        cliente.setEdad(45);
        cliente.setTelefono("+569-77776666");
        cliente.setCredito(100000);

        System.out.println("Nombre cliente: " + cliente.getNombre());
        System.out.println("Edad cliente: " + cliente.getEdad());
        System.out.println("Teléfono cliente: " + cliente.getTelefono());
        System.out.println("Crédito cliente: " + cliente.getCredito());
        
        //Parte 2: trabajador
        Trabajador trabajador = new Trabajador();
        
        trabajador.setNombre("Santiago");
        trabajador.setEdad(27);
        trabajador.setTelefono("+569-33221144");
        trabajador.setSalario(12000);

        System.out.println("\nNombre trabajador: " + trabajador.getNombre());
        System.out.println("Edad trabajador: " + trabajador.getEdad());
        System.out.println("Teléfono trabajador: " + trabajador.getTelefono());
        System.out.println("Salario trabajador: " + trabajador.getSalario());
    }
}
