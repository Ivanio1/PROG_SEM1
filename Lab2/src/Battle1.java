import pokemons.Komala;
import pokemons.Starmie;
import pokemons.*;
import ru.ifmo.se.pokemon.Battle;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Battle1 extends BattleGround{
    public static void main(String[] args) {
        JFrame window= new JFrame("Battle");
        window.setBounds(10,10,1300,1300);
        window.setLayout(null);
        window.setBackground(Color.PINK);
        window.setForeground(Color.PINK);
        //ввод
        JTextField Ally = new JTextField();
        JTextField Foe = new JTextField();

        Ally.setBounds(15,5,200,50);
        JLabel label=new JLabel("Ваш покемон (Введите имя и уровень в формате: Вася, 1)");
        label.setBounds(15,55,500,50);
        window.add(label);
        JLabel label1=new JLabel("Его противник (Введите имя и уровень в формате: Вася, 1)");
        label1.setBounds(800,65,500,50);
        window.add(label1);
        Foe.setBounds(800,5,200,50);
        window.add(Ally);
        window.add(Foe);

        JButton button = new JButton("В бой!");
        button.setBounds(150,300,200,50);
        button.setBackground(Color.GRAY);
        button.setForeground(Color.BLACK);
        window.add(button);
        ActionListener ALLY=new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                Battle battle=new Battle();
                String[] a,b;
                a=(String.valueOf(Ally.getText())).split(",");
                b=String.valueOf(Foe.getText()).split(",");
                Komala nam1=new Komala(a[0],Integer.parseInt(a[1]));
                Starmie nam2 = new Starmie(b[0],Integer.parseInt(b[1]));
                battle.addAlly(nam1);
                battle.addFoe(nam2);
                battle.go();
                JLabel label2=new JLabel();
                label2.setBounds(200,500,500,50);
                window.add(label2);

            }
        };
        button.addActionListener(ALLY);



        window.setVisible(true);

    }}

