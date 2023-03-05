import java.util.*;

public class Main
{
    public static void main(String[] args)
    {
        Employee[] staff = new Employee[3];

        staff[0] = new Employee("Harry", 40000);
        staff[1] = new Employee(60000);
        staff[2] = new Employee();

        for (Employee member : staff)
            System.out.println("name=" + member.getName() + ", id=" + member.getId() + ", salary=" + member.getSalary());
    }
}

class Employee
{
    private static int nextId;

    private int id;
    private String name;
    private double salary;

    static
    {
        var generator = new Random();
        nextId = generator.nextInt(10000);
    }

    {
        id = nextId;
        nextId++;
    }

    public Employee()
    {
        name = "";
        salary = 0.0;
    }

    public Employee(String name, double salary)
    {
        this.name = name;
        this.salary = salary;
    }

    public Employee(double salary)
    {
        this("Employee#" + nextId, salary);
    }

    public String getName()
    {
        return name;
    }

    public double getSalary()
    {
        return salary;
    }

    public int getId()
    {
        return id;
    }

    public String giveInfo()
    {
        return "Employee " + name + ", whose id is" + id + ", gets " + salary + "dollars every month.";
    }
}