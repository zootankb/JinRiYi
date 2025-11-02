using LiveCharts.Wpf;
using LiveCharts;
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
using System.Reflection.Emit;

namespace JinRiYi.Page
{
    /// <summary>
    /// LineWindow.xaml 的交互逻辑
    /// </summary>
    public partial class LineWindow : Window
    {
        public List<string> Labels { get; set; }
        public LineWindow()
        {
            InitializeComponent();

            Labels = new List<string> { "顾客1", "顾客2", "顾客3", "顾客4", "顾客5" };

            //SeriesCollection ls = new SeriesCollection();
            //double[] pieValues = new double[] { 25, 36, 85, 45, 69, 45, 85 };
            //for (int i = 0; i < pieValues.Length; i++)
            //{
            //    ls.Add(new LineSeries
            //    {
            //        Title = "商户 -- " + i,
            //        Values = new ChartValues<double> { pieValues[i] },
            //        DataLabels = true,
            //    });
            //}

            //this.Lvc1.DataContext = ls;
        }
    }
}
