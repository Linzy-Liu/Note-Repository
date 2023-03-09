import java.util.Arrays;

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

public class Uav implements Fly
{
    private int number;
    private static int nextUavId = 0;
    private double[] position;
    private double direction;
    private String name;

    {
        number = nextUavId++;
    }

    public Uav()
    {
        double[] temp_pos = {0.0, 0.0, 0.0};
        double temp_direct = 0.0; // (rho, theta)
        position = temp_pos;
        direction = temp_direct;
        name = "Uav";
    }

    public Uav(double direction)
    {
        this.position = new double[]{0.0, 0.0, 0.0};
        this.direction = direction;
        name = "Uav";
    }


    @Override
    public double[] up()
    {
        System.out.printf("No.%d %s is going up.\n", number, name);
        position[2] += 1.0;
        return this.position;
    }

    @Override
    public double[] up(int n)
    {
        System.out.printf("No.%d %s is going up.\n", number, name);
        position[2] += 1.0 * n;
        return this.position;
    }

    @Override
    public double[] down()
    {
        System.out.printf("No.%d %s is going down.\n", number, name);
        position[2] -= 1.0;
        return this.position;
    }

    @Override
    public double[] down(int n)
    {
        System.out.printf("No.%d %s is going down.\n", number, name);
        position[2] -= 1.0 * n;
        return this.position;
    }

    @Override
    public double[] forward()
    {
        System.out.printf("No.%d %s is going forward.\n", number, name);
        position[0] += Math.cos(direction);
        position[1] += Math.sin(direction);
        return this.position;
    }

    @Override
    public double[] forward(int n)
    {
        System.out.printf("No.%d %s is going forward.\n", number, name);
        position[0] += Math.cos(direction) * n;
        position[1] += Math.sin(direction) * n;
        return this.position;
    }

    @Override
    public double[] turn()
    {
        System.out.printf("No.%d %s is turning at %.3f degrees.\n", number, name, 90.0);
        this.direction += Math.PI / 2;
        this.direction %= 2 * Math.PI;
        return this.position;
    }

    @Override
    public double[] turn(double angle)
    {
        System.out.printf("No.%d %s is turning at %.3f degrees.\n", number, name, angle * 180 / Math.PI);
        this.direction += angle;
        this.direction %= 2 * Math.PI;
        return this.position;
    }

    public void setName(String name)
    {
        this.name = name;
    }

    public String getName()
    {
        return name;
    }

    public double[] getPosition()
    {
        return position;
    }

    public double getDirection()
    {
        return direction;
    }

    public int getNumber()
    {
        return number;
    }

    @Override
    public String toString()
    {
        return "Uav{" +
                "number=" + number +
                ", position=" + Arrays.toString(position) +
                ", direction=" + direction +
                ", name='" + name + '\'' +
                '}';
    }
}

class UavPlus extends Uav implements Camera
{
    private boolean isShootingVideo;

    public UavPlus()
    {
        super();
        setName("UavPlus");
        isShootingVideo = false;
    }

    public UavPlus(double direction)
    {
        super(direction);
        setName("UavPlus");
        isShootingVideo = false;
    }

    @Override
    public void photo()
    {
        System.out.printf("The photo has shot by No.%d %s.\n", getNumber(), getName());
    }

    @Override
    public void video()
    {
        if (isShootingVideo)
        {
            isShootingVideo = false;
            System.out.printf("No.%d %s has shot the video.\n", getNumber(), getName());
        }
        else
        {
            isShootingVideo = true;
            System.out.printf("No.%d %s is beginning to shoot the video.\n", getNumber(), getName());
        }
    }
}

class Debug
{
    public static void main(String[] args)
    {
        var uavs = new Uav[2];
        uavs[0] = new Uav();
        uavs[1] = new UavPlus();

        uavs[0].up(5);
        uavs[0].forward(3);
        uavs[0].down(2);
        uavs[1].turn();
        uavs[1].forward(6);
        UavPlus temp = (UavPlus) uavs[1];
        temp.photo();
        temp.video();
        temp.turn(Math.PI / 3);
        temp.forward(2);
        temp.video();

        System.out.println(uavs[0].toString());
        System.out.println(uavs[1].toString());
    }
}


