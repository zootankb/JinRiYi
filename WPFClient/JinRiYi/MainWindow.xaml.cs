using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace JinRiYi
{
    /// <summary>
    /// MainWindow.xaml 的交互逻辑
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            Init_Test_Data();
        }

        private void Init_Test_Data()
        {

            this.LstbUser.Items.Add("顾客1");
            this.LstbUser.Items.Add("顾客2");
            this.LstbUser.Items.Add("顾客3");
            this.LstbUser.Items.Add("顾客4");


            this.DgdUser.Columns.Clear();

            DataTable dt = new DataTable();
            dt.Columns.Add(new DataColumn("日期"));
            dt.Columns.Add(new DataColumn("项目"));
            dt.Columns.Add(new DataColumn("原价"));
            dt.Columns.Add(new DataColumn("折扣"));
            dt.Columns.Add(new DataColumn("折后价"));
            dt.Columns.Add(new DataColumn("对应师傅"));
            dt.Columns.Add(new DataColumn("剩余金额"));

            for (int i = 0; i < 5; i++)
            {
                var r = dt.Rows.Add();
                r[0] = "2025-09-07";
                r[1] = "全身按摩60分钟";
                r[2] = "100";
                r[3] = "0.85";
                r[4] = "85";
                r[5] = "1号师傅";
                r[6] = "888";
            }

            this.DgdUser.ItemsSource = dt.DefaultView;
        }

        private void BtnLineWindow_Click(object sender, RoutedEventArgs e)
        {
            new Page.LineWindow().Show();
        }

        private void BtnProjSetting_Click(object sender, RoutedEventArgs e)
        {
            new Page.ProjWindow().Show();
        }

        private void BtnRecharge_Click(object sender, RoutedEventArgs e)
        {
            new Page.RechargeWindow().Show();
        }

        private void BtnUserDetail_Click(object sender, RoutedEventArgs e)
        {

        }

        private void BtnExportExcel_Click(object sender, RoutedEventArgs e)
        {

        }

        private void BtnRemind_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("黄先生于2025年9月27号充1000元储蓄金，充卡送优惠充，1000享受所有项目0.78折的优惠（除去美甲美睫洗脸）今日宜推调理拿馆\r\n\r\n9月27号中式推拿60分钟\r\n1000-85.02=914.98（余额）");
        }
    }
}
