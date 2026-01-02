// pages/index/index.ts
let API = require('../../api')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    verification_code: "",
    verification_flag: "",
    radio_items: [
      {value: 0, name: "全部"},
    ],
    radio_selected_value: 1,
    radio_bg_color_normal: "#f2eada",
    radio_font_color_normal: "balck",
    radio_bg_color_selected: "#ff9300",
    radio_font_color_selected: "white",
    swiper_data: [
      "../../media/images/shop/products/spa.jpg",
      "../../media/images/shop/products/spa.jpg",
    ],
    product_items: [
      {
        product_type: 1,
        detail_items: [
          {
            img_url:  "../../media/images/shop/products/spa.png",
            title: "采耳30分钟|【店长采耳】逸静采耳/清爽放松",
            sale_info: "月销200+",
            praise_info: "200+觉得很赞",
            tag_info: "立冬 养生 全身 90分钟",
            ori_price: 159,
            exp_price: 122,
            vip_price: 119,
            buy_url: ""
          },{
            img_url:  "../../images/shop/products/spa.png",
            title: "采耳30分钟|【店长采耳】逸静采耳/清爽放松",
            sale_info: "月销200+",
            praise_info: "200+觉得很赞",
            tag_info: "立冬 养生 全身 90分钟",
            ori_price: 159,
            exp_price: 122,
            vip_price: 119,
            buy_url: ""
          }
        ]
      }
    ],
    show_product_items: Array<any>(),
    showDialog: false,
    showDialogImage: false,
    showDialogImageUrl: "",
    showDialogVideo: false,
    showDialogVideoUrl: "",
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    console.log(options)
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {
    // wx.navigateTo({
    //   url: "/pages/feedback/feedback"
    // });
    this.get_main_data();
    this.getDialogAd();
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {
    let app = getApp();
    app.globalData;
    // 没有值代表管理员界面
    if(this.data.verification_code) {
      // 有值则判断是否有效
      wx.request({
        url: app.exports.StartFeedback + `${this.data.verification_code}/`, // 接口地址
        method: 'POST', // 请求方法
        data: {
          verification_code: "29728760"
        },
        header: {
          'content-type': 'application/x-www-form-urlencoded' // 设置请求头
        },
        success(res) {
          console.log('请求成功:', res.data); // 打印返回数据
        },
        fail(err) {
          console.error('请求失败:', err); // 打印错误信息
        }
      });
      // 1.有效则显示反馈界面
      // 2.无效则用页面警告已经用过
    }
    // 展示信息
    console.log("展示信息用的value：", this.data.radio_items[0].value)
    // this.update_product_type(0);
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {
    const that = this
    let path_cont = `/pages/feedback/index?verification_code=${that.
      data.verification_code}`;
    console.log(path_cont);
    return {
      title: "今日宜反馈",
      path: path_cont,
      desc: '反馈内容',
      success(res: any) {
        console.log('分享成功', res)
        // 可以在这里记录分享成功的数据
        wx.showToast({
          title: '分享成功',
          icon: 'success'
        })
      },
      fail(err: any) {
        console.log('分享失败', err)
      }
    }
  },
  onToWriteFeedback() {
    wx.navigateTo({
      url: "/pages/feedback/feedback"
    });
  },
  onShare2Friend() {
    // 分享给好友
    // wx.shareMessageToFriend({
    //   openId: '好友的openId',
    //   title: '分享标题',
    //   imageUrl: '分享图片URL',
    //   success(res) {
    //     console.log('分享成功', res)
    //   },
    //   fail(err) {
    //     console.log('分享失败', err)
    //   }
    // });
  },
  onCreateVerification() {
    console.log("获取验证码")
    let app = getApp();
    const that = this;
    wx.request({
      url: app.exports.GetVersionCode, // 接口地址
      method: 'GET', // 请求方法
      timeout: 5000,
      header: {
        'content-type': 'application/json' // 设置请求头
      },
      success(res) {
        console.log('请求成功:', res.data); // 打印返回数据
        that.setData({
          verification_code: res.data.data.msg
        });
      },
      fail(err) {
        console.error('请求失败:', err); // 打印错误信息
        wx.showModal({
          title: "提示",
          content: "获取异常，请重新获取",
          showCancel: false,
          confirmText: "确定",
          success: function (res) {
            if (res.confirm) {
              console.log('确定');
            }
          }
        })
      }
    });
    console.log("已经发送获取验证码请求")
  },
  onCheckVerification() {
    console.log(API.exports.GetAllProducts);
    return;
    let app = getApp();
    const that = this;
    console.log(JSON.stringify({
      verification_code: "29728760"
    }));
    wx.request({
      url: app.globalData.CheckVerificationValid, // 接口地址
      method: 'GET', // 请求方法
      data: {
        verification_code: that.data.verification_code
      },
      header: {
        'content-type': 'application/json' // 设置请求头
      },
      dataType: "json",
      success(res) {
        console.log('请求成功:', res.data); // 打印返回数据
        console.log('请求成功:', res.data.data.msg); // 打印返回数据
        that.setData({
          verification_flag: res.data.data.msg
        });
      },
      fail(err) {
        console.error('请求失败:', err); // 打印错误信息
        wx.showModal({
          title: "提示",
          content: "获取异常，请重新获取",
          showCancel: false,
          confirmText: "确定",
          success: function (res) {
            if (res.confirm) {
              console.log('确定');
            }
          }
        })
      }
    });
    console.log("已经发送验证数据");
  },
  get_main_data() {
    let that = this;
    wx.request({
      url: API.GetMainData, // 接口地址
      method: 'GET', // 请求方法
      header: {
        'content-type': 'application/json' // 设置请求头
      },
      dataType: "json",
      success(res) {
        const data = res.data;
        console.log("请求成功主体数据：", data);
        let main_data = data as MainData;
        let radio_items = [];
        radio_items.push({
          value: 0, 
          name: "全部"
        });
        let all_proj_data: Array<ProjData> = [];
        main_data.product_items.forEach((val, index) => {
          all_proj_data = all_proj_data.concat(val.detail_items)
          radio_items.push({
            value: val.product_type, 
            name: val.product_type_name
          });
        });
        that.setData({
          swiper_data: main_data.swiper_data,
          product_items: main_data.product_items,
          radio_items: radio_items
        });
        console.log("设置好了滚动数据：", main_data.swiper_data);
        console.log("设置好了项目数据：", main_data.product_items);
        console.log("设置好了类型数据：", radio_items);
        that.update_product_type(0);
      },
      fail(err) {
        console.error('请求失败:', err); // 打印错误信息
        wx.showModal({
          title: "提示",
          content: "获取异常，请重新获取",
          showCancel: false,
          confirmText: "确定",
          success: function (res) {
            if (res.confirm) {
              console.log('确定重新获取');
            }
          }
        })
      }
    });
  },
  product_type_changed(e) {
    let selectValue = e.currentTarget.dataset.bid;
    this.update_product_type(selectValue);
  },
  update_product_type(type_value: number) {
    console.log("当前的类型值："+this.data.radio_selected_value);
    console.log("选择的类型值："+type_value);
    this.setData({
      radio_selected_value: type_value
    });
    // TODO
    // 要更新显示内容
    if (type_value == 0) {
      // 全部
      this.setData({
        show_product_items: this.data.product_items
      })
    } else {
      // 过滤
      let showItems = Array<any>();
      this.data.product_items.forEach(element => {
        if (element.product_type == type_value) {
          showItems.push(element)
        }
      });
      this.setData({
        show_product_items: showItems
      })
    }
  },
  toggleDialog() {
    this.setData({
      showDialog: false
    });
  },
  getDialogAd() {
    let that = this;
    wx.request({
      url: API.DialogAD, // 接口地址
      method: 'GET', // 请求方法
      header: {
        'content-type': 'application/json' // 设置请求头
      },
      dataType: "json",
      success(res) {
        const data = res.data;
        console.log("请求广告成功主体数据：", data);
        let adData = data as DialogAd;
        if (adData.is_file) {
          that.setData({
            showDialog:  true,
            showDialogImage: true,
            showDialogImageUrl: adData.res_path
          });
        } else {
          that.setData({
            showDialog:  true,
            showDialogVideo: true,
            showDialogVideoUrl: adData.res_path
          });
        }
      },
      fail(err) {
        that.setData({
          showDialog: false
        })
      }
    });
  }
})