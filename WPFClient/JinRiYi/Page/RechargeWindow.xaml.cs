using System;
using System.Collections.Generic;
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
using System.Windows.Shapes;

namespace JinRiYi.Page
{
    /// <summary>
    /// RechargeWindow.xaml 的交互逻辑
    /// </summary>
    public partial class RechargeWindow : Window
    {
        public RechargeWindow()
        {
            InitializeComponent();

            this.LstbUsers.Items.Add("顾客1");
            this.LstbUsers.Items.Add("顾客2");
            this.LstbUsers.Items.Add("顾客3");
            this.LstbUsers.Items.Add("顾客4");
            this.LstbUsers.Items.Add("顾客2");

            this.LstbRecords.Items.Add("2019-01-01 10:00:00 充值100元, 余额1000元");
            this.LstbRecords.Items.Add("2019-01-02 10:00:00 充值200元, 余额1200元");
            this.LstbRecords.Items.Add("2019-01-03 10:00:00 充值300元, 余额1500元");
            this.LstbRecords.Items.Add("2019-01-04 10:00:00 充值400元, 余额1900元");
            this.LstbRecords.Items.Add("2019-01-05 10:00:00 充值500元, 余额2400元");
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {

        }
    }
}
