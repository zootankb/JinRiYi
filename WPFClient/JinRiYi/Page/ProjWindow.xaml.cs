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
    /// ProjWindow.xaml 的交互逻辑
    /// </summary>
    public partial class ProjWindow : Window
    {
        public ProjWindow()
        {
            InitializeComponent();

            ProjLst.Items.Add("推拿");
            ProjLst.Items.Add("采耳");
            ProjLst.Items.Add("汗蒸");
            ProjLst.Items.Add("刮痧");
            ProjLst.Items.Add("拔罐");
        }
    }
}
