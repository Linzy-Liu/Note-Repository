public class Uav implements Fly
{
    private int number;
    private static int nextId = 0;
    private double[] position;
    private double[] direction;

    {
        number = nextId++;
    }

    public Uav()
    {
        double[] temp_pos = {0.0, 0.0, 0.0};
        double[] temp_direct = {1.0, 0.0}; // (rho, theta)
        position = temp_pos;
        direction = temp_direct;
    }

    public Uav(double[] direction)
    {
        this.position = new double[]{0.0, 0.0, 0.0};
        if (direction.length != 2)
        {
            System.out.println("The length of direction is 2 but given " + direction.length + ", please reset Uav's direction");
            this.direction = null;
        }
        else
            this.direction = direction;
    }


    @Override
    public double[] up()
    {
        System.out.printf("No.%d Uav is going up.\n", number);
        position[2] += 1.0;
        return this.position;
    }

    @Override
    public double[] up(int n)
    {
        System.out.printf("No.%d Uav is going up.\n", number);
        position[2] += 1.0 * n;
        return this.position;
    }

    @Override
    public double[] down()
    {
        return new double[0];
    }

    @Override
    public double[] down(int n)
    {
        return new double[0];
    }

    @Override
    public double[] forward()
    {
        return new double[0];
    }

    @Override
    public double[] forward(int n)
    {
        return new double[0];
    }

    @Override
    public double[] turn()
    {
        return new double[0];
    }

    @Override
    public double[] turn(double angle)
    {
        return new double[0];
    }
}

interface Fly
{
    double[] up();

    double[] up(int n);

    double[] down();

    double[] down(int n);

    double[] forward();

    double[] forward(int n);

    double[] turn();

    double[] turn(double angle);
}

interface Camera
{
    void photo();

    void video();
}


