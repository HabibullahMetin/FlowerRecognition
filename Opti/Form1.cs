using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Optimizasyon
{
    public partial class Form1 : Form
    {
        public TextBox[,] TextKutu;
        public TextBox[] arzKutu;
        public TextBox[] talepKutu;
        public int arzMiktar;
        public int talepMiktar;
        public int left;
        public int top;
        public int leftLabelArz;
        public int topLabelArz;
        public int leftLabelTalep;
        public int topLabelTalep;
        Button b1, b2;
        TextBox t1, t2;

        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            arayuzOlustur();
            this.WindowState = FormWindowState.Maximized;
        }
        private void arayuzOlustur()
        {
            //Arz talep textbox uretilemesi
            left = 80;
            top = 100;

            //Arz label olusturulmasi
            leftLabelArz = 30;
            topLabelArz = 100;

            //talep label olusturulmasi
            leftLabelTalep = 80;
            topLabelTalep = 70;

            Label l1, l2;

            b1 = new Button();
            b1.Name = "button1";
            b1.Text = "Oluştur";
            b1.Left = 15;
            b1.Top = 15;
            b1.Width = 75;
            b1.Height = 25;
            b1.Click += olustur_Click;
            Controls.Add(b1);

            b2 = new Button();
            b2.Name = "button2";
            b2.Text = "Hesapla";
            b2.Enabled = false;
            b2.Left = 110;
            b2.Top = 15;
            b2.Width = 75;
            b2.Height = 25;
            b2.Click += hesapla_Click;
            Controls.Add(b2);

            l1 = new Label();
            l1.Text = "Arz   :";
            l1.Left = 210;
            l1.Top = 10;
            l1.Width = 35;
            l1.Height = 15;
            Controls.Add(l1);

            l2 = new Label();
            l2.Text = "Talep   :";
            l2.Left = 210;
            l2.Top = 40;
            l2.Width = 50;
            l2.Height = 15;
            Controls.Add(l2);

            t1 = new TextBox();
            t1.Name = "textBox1";
            t1.Left = 270;
            t1.Top = 10;
            t1.Width = 95;
            t1.Height = 20;
            Controls.Add(t1);

            t2 = new TextBox();
            t2.Name = "textBox2";
            t2.Left = 270;
            t2.Top = 40;
            t2.Width = 95;
            t2.Height = 20;
            Controls.Add(t2);
        }
        private void arzLabelOlustur()
        {
            Label label;

            for (int i = 0; i < arzMiktar; i++)//arz listesi
            {
                label = new Label();
                label.Left = leftLabelArz;
                label.Top = topLabelArz;
                label.Text = (i + 1) + ".Arz";
                label.Width = 50;
                label.Height = 30;
                Controls.Add(label);
                topLabelArz += 30;
            }

            //talep miktar label
            label = new Label();
            label.Left = 10;
            label.Top = topLabelArz;
            label.Text = "Talep Miktar";
            label.Width = 70;
            label.Height = 30;
            Controls.Add(label);
        }
        private void talepLabelOlustur()
        {
            Label label;
            for (int i = 0; i < talepMiktar; i++)
            {
                label = new Label();
                label.Left = leftLabelTalep;
                label.Top = topLabelTalep;
                label.Text = (i + 1) + ".Talep";
                label.Width = 50;
                label.Height = 30;
                Controls.Add(label);
                leftLabelTalep += 50;
            }

            label = new Label();
            label.Left = leftLabelTalep+10;
            label.Top = topLabelTalep;
            label.Text = "Arz Miktar";
            label.Width = 100;
            label.Height = 30;
            Controls.Add(label);

        }
        private void arzTalepTextboxOlustur()
        {
            int sayacArz = 0;
            int sayacTalep = 0;

            TextKutu = new TextBox[arzMiktar, talepMiktar];
            arzKutu = new TextBox[arzMiktar];
            talepKutu = new TextBox[talepMiktar];

            arzLabelOlustur();
            talepLabelOlustur();

            for (int i = 0; i < arzMiktar; i++)
            {
                for (int j = 0; j < talepMiktar; j++)
                {
                    TextKutu[i, j] = new TextBox();
                    TextKutu[i, j].Left = left;
                    TextKutu[i, j].Top = top;
                    TextKutu[i, j].Width = 50;
                    TextKutu[i, j].Text = "";
                    this.Controls.Add(TextKutu[i, j]);
                    left += 50;
                }

                arzKutu[sayacArz] = new TextBox();
                arzKutu[sayacArz].Left = left+10;
                arzKutu[sayacArz].Top = top;
                arzKutu[sayacArz].Width = 50;
                arzKutu[sayacArz].Text = "";
                this.Controls.Add(arzKutu[sayacArz]);
                sayacArz++;

                top = top + 30;
                left = 80;
            }

            for(int i = 0; i < talepMiktar; i++)
            {
                talepKutu[sayacTalep] = new TextBox();
                talepKutu[sayacTalep].Left = left;
                talepKutu[sayacTalep].Top = top;
                talepKutu[sayacTalep].Width = 50;
                talepKutu[sayacTalep].Text = "";
                this.Controls.Add(talepKutu[sayacTalep]);
                left += 50;
                sayacTalep++;
            }

        }
        private void olustur_Click(object sender, EventArgs e)
        {
            arzMiktar = Convert.ToInt32(t1.Text);
            talepMiktar = Convert.ToInt32(t2.Text);
            b1.Enabled = false;
            t1.Enabled = false;
            t2.Enabled = false;
            b2.Enabled = true;
            arzTalepTextboxOlustur();
        }
        private void hesapla_Click(object sender, EventArgs e)
        {
            bool[,] atamaMaskesi = new bool[arzMiktar, talepMiktar];
            int minimumDeger = int.MaxValue;
            int deger;
            int sayacDongu = 0,sayacTalep,sayacMaske;
            int atamaX=0, atamaY=0;
            int totalMaliyet = 0;
            int minimumArzTalep = 0;
            string sonuc = "ATAMALAR\n\n";

            //atama maskesi olusturma
            for (int i = 0; i < arzMiktar; i++) for (int j = 0; j < talepMiktar; j++) atamaMaskesi[i, j] = false;

            do
            {
                //talepler sifir kontrolu
                sayacTalep = 0;
                for (int i = 0; i < talepMiktar; i++)
                {
                    if (Convert.ToInt32(talepKutu[i].Text) != 0)
                    {
                        sayacTalep++;
                    }else
                    {
                        for (int j = 0; j < arzMiktar; j++) atamaMaskesi[j, i] = true; //eger 0 ise sutun atanmis olur
                    }
                }
                if (sayacTalep == 0) break;
                //-----

                //butun dizi atama kontrolu
                sayacMaske = 0;
                for (int i = 0; i < arzMiktar; i++)
                {
                    for (int j = 0; j < talepMiktar; j++)
                    {
                        if (atamaMaskesi[j, i] == false) sayacMaske++;
                    }
                }
                if (sayacMaske == 0) break;
                //-----

                //minimumum bulunmasi
                for (int i = 0; i < arzMiktar; i++)
                {
                    for (int j = 0; j < talepMiktar; j++)
                    {
                        deger = Convert.ToInt32(TextKutu[i, j].Text);
                        if (atamaMaskesi[i, j] == false && deger < minimumDeger)
                        {
                            atamaX = i;
                            atamaY = j;
                            minimumDeger = deger;
                        }
                    }
                }
                //-----

                //talep arz minimumun bulunmasi ve yeni degerlerin atanmalari
                if (Convert.ToInt32(arzKutu[atamaX].Text) < Convert.ToInt32(talepKutu[atamaY].Text))
                {
                    talepKutu[atamaY].Text = "" + (Convert.ToInt32(talepKutu[atamaY].Text) - Convert.ToInt32(arzKutu[atamaX].Text));
                    minimumArzTalep = Convert.ToInt32(arzKutu[atamaX].Text);
                    sonuc += (atamaX+1) + ".Arz - " + (atamaY+1) + ".Talep: " + minimumArzTalep + "\n";
                    arzKutu[atamaX].Text = "0";
                }else{
                    arzKutu[atamaX].Text = "" + (Convert.ToInt32(arzKutu[atamaX].Text) - Convert.ToInt32(talepKutu[atamaY].Text));
                    minimumArzTalep = Convert.ToInt32(talepKutu[atamaY].Text);
                    sonuc += (atamaX + 1) + ".Arz - " + (atamaY + 1) + ".Talep: " + minimumArzTalep + "\n";
                    talepKutu[atamaY].Text = "0";
                }
                //-----

                //maliyet hesabi
                totalMaliyet += minimumArzTalep * minimumDeger;

                //atananin dizide kaydedilmesi
                atamaMaskesi[atamaX, atamaY] = true;
                sayacDongu++;

                MessageBox.Show("En Küçük("+ sayacDongu + "): " + minimumDeger);
                minimumDeger = int.MaxValue;
            } while (true);

            MessageBox.Show("Minimum Maliyet: "+ totalMaliyet);
            MessageBox.Show(sonuc);

            Controls.Clear();
            arayuzOlustur();
        }
    }
}
