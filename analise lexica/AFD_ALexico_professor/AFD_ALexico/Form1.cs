using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AFD_ALexico
{
    public partial class Form1 : Form
    {
        String arquivoConfiguracao;
        String[] estados, simbolos, transicoes,estadosFinais;
        LinkedList<string> lista_transicoes = new LinkedList<string>();
        char[] ctermo;
        int indexador = 0, firstClick=0;

        public void passoApasso()
        {
            if (indexador < ctermo.Length)
            {
                label3.Text = ctermo[indexador].ToString();
                label2.Text = estadoAtual;
                String search = label2.Text + ":" + label3.Text;
                Console.Write("Search: " + search);
                String regra = "";
                for(int i = 0; i < transicoes.Length; i++)
                {
                    if (transicoes.ElementAt(i).StartsWith(search))
                    {
                        regra = transicoes.ElementAt(i);
                        estadoAtual = regra.Split(':')[2];
                    }
                }
                Console.WriteLine("Regra encontrada: "+regra);
                if (regra.Equals(""))
                {
                    estadoAtual = "x";//qualquer coisa aqui para não reconhecer mesmo.
                    label4.Text = "Termo não reconhecido";
                    button3.Enabled = false;
                    button2.Enabled = false;
                }

                
                indexador++;
            }
            else
            {
                //TODO LER ESTADOS FINAIS
                String estadoTerminal;
                for (int y = 0; y < estadosFinais.Length; y++)
                {
                    if (estadosFinais.ElementAt(y).StartsWith(estadoAtual))
                    {
                        estadoTerminal = estadosFinais.ElementAt(y).Split('>')[1];
                        label4.Text = estadoTerminal;
                        button3.Enabled = false;
                    }
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            String termo = textBox1.Text;
            ctermo = termo.ToCharArray();
            for (int x = 0; x <= ctermo.Length; x++)
            {
                passoApasso();
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (firstClick == 0)
            {
                String termo = textBox1.Text;
                ctermo = termo.ToCharArray();
                firstClick++;
                textBox1.Enabled = false;
                passoApasso();
            }
            else
            {
                passoApasso();
            }
            Console.WriteLine("indexador: " + indexador);

        }

        String estadoAtual;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "AFD config files (*.txt)|*.txt";
            openFileDialog1.ShowDialog();
            arquivoConfiguracao = openFileDialog1.FileName;

            StreamReader leitor = new StreamReader(arquivoConfiguracao);
            int numLinha = 1;
            while (!leitor.EndOfStream)
            {
                String linha = leitor.ReadLine();
                if (numLinha == 1)
                {//estou lendo os símbolos do AFD
                    simbolos = linha.Split(',');
                    Console.WriteLine("AFD com " + simbolos.Length + " símbolos.");
                }
                if(numLinha == 2)
                {//estou lendo os estados do AFD
                    estados = linha.Split(',');
                    Console.WriteLine("AFD com " + estados.Length + " estados.");
                }
                if (numLinha == 3)
                {//estado atual inicia em estado inicial
                    estadoAtual = linha;
                }
                if(numLinha == 4)
                {//armazeno os estados finais
                    estadosFinais = linha.Split(',');
                    Console.WriteLine("AFD com " + estadosFinais.Length + " estados finais.");
                }
                if(numLinha >= 5)
                {//TODO melhorar
                    transicoes = linha.Split(',');
                    inserelista(transicoes);
                    MessageBox.Show("AFD com " + lista_transicoes.Count() + " regras de transição.");
                }
                Console.WriteLine(linha);
                numLinha++;
                textBox1.Enabled = true;
                
            }
        }

        public void inserelista(String[] lista)
        {
            for (int i = 0; i < lista.Length; i++)
            {
                lista_transicoes.AddLast(lista[i]);
                //MessageBox.Show(lista[i]);
            }


        }

    }
}
