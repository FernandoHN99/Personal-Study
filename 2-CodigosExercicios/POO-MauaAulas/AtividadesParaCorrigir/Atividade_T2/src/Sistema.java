// Fernando Henriques Neto
// RA:18.00931-0

import java.util.ArrayList;
import java.util.List;

public class Sistema {
    public void run(){
        Util.clearScreen();
        List<Membro> Membros = new ArrayList<Membro>();
        
        Membro membro1 = new BigBrothers("BihBrother1", "BihBrother1@gmail.com");
        Membros.add(membro1);

        Membro membro2 = new MobileMembers("MobileMember1", "MobileMember1@gmail.com");
        Membros.add(membro2);

        Membro membro3 = new HeavyLifters("HeavyLifters1", "HeavyLifters@gmail.com");
        Membros.add(membro3);
        
        Membro membro4 = new ScriptGuys("ScriptGuys1", "ScriptGuys@gmail.com");
        Membros.add(membro4);

        Membro membro5 = new HeavyLifters("HeavyLifters2", "HeavyLifters2@gmail.com");
        Membros.add(membro5);

        Membro membro6 = new ScriptGuys("ScriptGuys2", "ScriptGuys2@gmail.com");
        Membros.add(membro6);

        System.out.println("\nTodos os membros");
        mostrarMembros(Membros);

        System.out.println("\nPrimeira Exclusão");
        excluirMembro(Membros, "HeavyLifters", 1);
        mostrarMembros(Membros);
        
        System.out.println("\nSegunda Exclusão");
        excluirMembro(Membros, "ScriptGuys", 2);
        mostrarMembros(Membros);
        
    }

    private void mostrarMembros(List<Membro> listMembros){
        for (Membro membro : listMembros) {
            System.out.println(membro);
        }
    }

    private void excluirMembro(List<Membro> listMembros, String funcaoMembro, int position){
        int counter = 0;
        for (int i = 0; i < listMembros.size(); i++) {
            if(listMembros.get(i).getFuncao().equals(funcaoMembro)){
                counter+=1;
                if(counter == 1){
                    listMembros.remove(i);
                    break;
                }
            }
        }
    }




}
