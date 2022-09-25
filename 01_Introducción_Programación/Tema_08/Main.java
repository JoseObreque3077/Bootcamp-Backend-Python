public class Main {
    public static void main(String[] args) {
        Persona persona = new Persona();

        persona.setNombre("Eduardo");
        persona.setEdad(30);
        persona.setTelefono("+569-77665544");

        System.out.println("Nombre: " + persona.getNombre());
        System.out.println("Edad: " + persona.getEdad());
        System.out.println("Teléfono: " + persona.getTelefono());
    }
}
