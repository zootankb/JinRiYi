// pages/index/index.ts
Page({

  /**
   * 页面的初始数据
   */
  data: {
    verification_code: "",
    verification_flag: ""
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
    wx.navigateTo({
      url: "/pages/feedback/feedback"
    });
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
        url: `http://192.168.1.2:8000/feedback/${this.data.verification_code}/`, // 接口地址
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
    const that = this;
    wx.request({
      url: 'http://192.168.1.2:8000/feedback/get_verification_code/', // 接口地址
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
    return;
    const that = this;
    console.log(JSON.stringify({
      verification_code: "29728760"
    }));
    wx.request({
      url: 'http://192.168.1.2:8000/feedback/check_verification_valid/', // 接口地址
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
  }
})