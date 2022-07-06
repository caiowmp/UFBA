public class Sistema
{
    private static Sistema instance = new Sistema();

    private Sistema(){ }

    public static Sistema getInstance()
    {
        return this.instance;
    }

}