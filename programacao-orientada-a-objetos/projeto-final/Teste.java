package Aplicação;

import Classes.*;
import java.util.ArrayList;
import java.util.Scanner;

public class Teste{
    public static void listarJogadores(Jogo jogo){
        jogo.listarJogadores();
    }

    public static void listarIniciantes(Jogo jogo){
        jogo.listarIniciantes();
    }

    public static void listarAmadores(Jogo jogo){
        jogo.listarAmadores();
    }

    public static void listarProfissionais(Jogo jogo){
        jogo.listarProfissionais();
    }

    public static void listarEstrelas(Jogo jogo){
        jogo.listarEstrelas();
    }

    public static void ganha(Jogo jogo){
        jogo.ganha();
    }

    public static void perde(Jogo jogo){
        jogo.perde();
    }

    public static void novaSkin(Jogo jogo){
        for(Jogador item : jogo.getPlayers()){
            if(item instanceof Profissional){
                jogo.novaSkin((Profissional) item); //Casting
            }
        }
    }

    public static void addJogador(Jogo jogo){
        jogo.addJogador();
    }

    public static void trocarSkin(Jogo jogo){
        for(Jogador item : jogo.getPlayers()){
            if(item instanceof Profissional){
                jogo.trocarSkin((Profissional) item); //Casting
            }
        }
    }
}
