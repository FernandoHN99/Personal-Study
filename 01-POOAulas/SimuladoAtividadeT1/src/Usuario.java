import java.util.*;

public class Usuario {
    private String nome;
    private String senha;
    private String email;
    private List<String> listQRCodes;

    public Usuario(String nome, String email, String senha){
        this.nome = nome;
        this.senha = senha;
        this.email = email;
        this.listQRCodes = new ArrayList();
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public List<String> getListQRCodes() {
        return listQRCodes;
    }

    public void setListQRCodes(String QRCode) {
        this.listQRCodes.add(QRCode);
    }

    public Integer checkQRCode(String QRCode){
        return this.listQRCodes.indexOf(QRCode);
    }
}
