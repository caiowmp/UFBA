package Aplicação;

import Classes.*;
import java.util.ArrayList;

interface JogoGenerico{

     String getNomeJogo();
     void setNomeJogo(String nome);
     ArrayList<Jogador> getPlayers();
     void listarJogadores();

     void listarIniciantes();

     void listarAmadores();

     void listarProfissionais();

     void listarEstrelas();

     void ganha();

     void perde();

     void novaSkin(Profissional j);

     void addJogador();
     
     void trocarSkin(Profissional j);
}