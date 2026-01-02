let API = require('../../api')
Component({
  data: {
    userInfo: {},
    hasUserInfo: false,
    canIUseGetUserProfile: wx.canIUse('getUserProfile'),
    canIUseNicknameComp: wx.canIUse('input.type.nickname'),
    title: {
      zhhans_title: "顾客意见卡",
      enus_title: "GUEST OPTIOON QUESTIONNAIRE",
    },
    desc: {
      line1: "尊敬的顾客：\n&emsp;&emsp;您好！感谢您的光临，为了给您提供更亲切舒适的服务和消费空间，希望您能为本店提出宝贵的意见，感谢支持！",
    },
    projNameArr: [],
    projIdArr: [],
    selectedProjIdx: -1,
    thankDesc: "&emsp;&emsp;我们珍惜每一条评价，用心对待每一份的信任和选择，我们继续努力加油，期待您的常来！",
    starImgPaths_StarSvrPro0: "../../media/images/small/small_level_0_normal.png",
    starImgPaths_StarSvrPro1: "../../media/images/small/small_level_1_normal.png",
    starImgPaths_StarSvrPro2: "../../media/images/small/small_level_2_normal.png",
    starImgPaths_StarSvrPro3: "../../media/images/small/small_level_3_selected.png",
    starImgPaths_StarTecPro0: "../../media/images/small/small_level_0_normal.png",
    starImgPaths_StarTecPro1: "../../media/images/small/small_level_1_normal.png",
    starImgPaths_StarTecPro2: "../../media/images/small/small_level_2_normal.png",
    starImgPaths_StarTecPro3: "../../media/images/small/small_level_3_selected.png",
    starImgPaths_StarEnvPro0: "../../media/images/small/small_level_0_normal.png",
    starImgPaths_StarEnvPro1: "../../media/images/small/small_level_1_normal.png",
    starImgPaths_StarEnvPro2: "../../media/images/small/small_level_2_normal.png",
    starImgPaths_StarEnvPro3: "../../media/images/small/small_level_3_selected.png",
    selectStarSvrNum: 4,
    selectStarTecNum: 4,
    selectStarEnvNum: 4,
    tecName: "",
    sugContent: "",
  },
  methods: {
    onLoad(options: any) {
      console.log(options)
      console.log("API内容");
      console.log(API.GetAllProducts);
      console.log(API.StartFeedback);
    },
     /**
   * 生命周期函数--监听页面初次渲染完成
   */
    onReady() {
      // 拉取项目
      console.log("拉取项目")
      let that = this;
      wx.request({
        url: API.GetAllProducts, // 接口地址
        method: 'GET', // 请求方法
        header: {
          'content-type': 'application/json' // 设置请求头
        },
        success(res) {
          console.log('请求成功:', res.data); // 打印返回数据
          let ids: number[] = [];
          let names: string[] = [];
          res.data.forEach(item => {
            ids.push(item.id);
            names.push(item.name);
          });
          that.setData({
            projNameArr: names,
            projIdArr: ids,
            selectedProjIdx: 0
          });
          console.log("以获取项目数据");
        },
        fail(err) {
          console.error('请求失败:', err); // 打印错误信息
        }
        });
    },
    onTextareaBlurTec(e: { detail: { value: any } }) {
      this.setData({
        tecName: e.detail.value
      })
    },
    onTextareaContent(e: { detail: { value: any } }) {
      this.setData({
        sugContent: e.detail.value
      })
    },
    // 事件处理函数
    bindViewTap() {
      wx.navigateTo({
        url: '../logs/logs',
      })
    },
    getUserProfile() {
      // 推荐使用wx.getUserProfile获取用户信息，开发者每次通过该接口获取用户个人信息均需用户确认，开发者妥善保管用户快速填写的头像昵称，避免重复弹窗
      const that = this;
      wx.getUserProfile({
        desc: '展示用户信息', // 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
        success: (res) => {
          console.log(res)
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          });
          wx.showModal({
            title: '提示',
            content: '请确认提交反馈和建议',
            success: function (res) {
              if (res.confirm) {
                console.log("获取到的用户名字：" + that.data.userInfo.nickName);
                that.onCommit();
              } else {
                console.log('用户点击取消');
              }
            }
            });
        },
        fail: () => {
          wx.showToast({
            title: '获取用户信息失败，请重新点击提交',
            icon: 'success',
            duration: 2000
            });
        }
      })
    },
    onProjChanged(e: { detail: { value: number } }) {
      console.log(e.detail.value);
      this.data.selectedProjIdx = e.detail.value;
      this.setData({
        selectedProjIdx: e.detail.value
      });
    },
    starSvrPro0() {
      this.data.selectStarSvrNum = 1;
      console.log(this.data.selectStarSvrNum);
      this.setData({
        starImgPaths_StarSvrPro0: "../../media/images/small/small_level_0_selected.png",
        starImgPaths_StarSvrPro1: "../../media/images/small/small_level_1_normal.png",
        starImgPaths_StarSvrPro2: "../../media/images/small/small_level_2_normal.png",
        starImgPaths_StarSvrPro3: "../../media/images/small/small_level_3_normal.png"
      });
    },
    starSvrPro1() {
      this.data.selectStarSvrNum = 2;
      console.log(this.data.selectStarSvrNum);
      this.setData({
        starImgPaths_StarSvrPro0: "../../media/images/small/small_level_0_normal.png",
        starImgPaths_StarSvrPro1: "../../media/images/small/small_level_1_selected.png",
        starImgPaths_StarSvrPro2: "../../media/images/small/small_level_2_normal.png",
        starImgPaths_StarSvrPro3: "../../media/images/small/small_level_3_normal.png"
      });
    },
    starSvrPro2() {
      this.data.selectStarSvrNum = 3;
      console.log(this.data.selectStarSvrNum);
      this.setData({
        starImgPaths_StarSvrPro0: "../../media/images/small/small_level_0_normal.png",
        starImgPaths_StarSvrPro1: "../../media/images/small/small_level_1_normal.png",
        starImgPaths_StarSvrPro2: "../../media/images/small/small_level_2_selected.png",
        starImgPaths_StarSvrPro3: "../../media/images/small/small_level_3_normal.png"
      });
    },
    starSvrPro3() {
      this.data.selectStarSvrNum = 4;
      console.log(this.data.selectStarSvrNum);
      this.setData({
        starImgPaths_StarSvrPro0: "../../media/images/small/small_level_0_normal.png",
        starImgPaths_StarSvrPro1: "../../media/images/small/small_level_1_normal.png",
        starImgPaths_StarSvrPro2: "../../media/images/small/small_level_2_normal.png",
        starImgPaths_StarSvrPro3: "../../media/images/small/small_level_3_selected.png"
      });
    },
    starTecPro0() {
      this.data.selectStarTecNum = 1;
      console.log(this.data.selectStarTecNum);
      this.setData({
        starImgPaths_StarTecPro0: "../../media/images/small/small_level_0_selected.png",
        starImgPaths_StarTecPro1: "../../media/images/small/small_level_1_normal.png",
        starImgPaths_StarTecPro2: "../../media/images/small/small_level_2_normal.png",
        starImgPaths_StarTecPro3: "../../media/images/small/small_level_3_normal.png"
      });
    },
    starTecPro1() {
      this.data.selectStarTecNum = 2;
      console.log(this.data.selectStarTecNum);
      this.setData({
        starImgPaths_StarTecPro0: "../../media/images/small/small_level_0_normal.png",
        starImgPaths_StarTecPro1: "../../media/images/small/small_level_1_selected.png",
        starImgPaths_StarTecPro2: "../../media/images/small/small_level_2_normal.png",
        starImgPaths_StarTecPro3: "../../media/images/small/small_level_3_normal.png"
      });
    },
    starTecPro2() {
      this.data.selectStarTecNum = 3;
      console.log(this.data.selectStarTecNum);
      this.setData({
        starImgPaths_StarTecPro0: "../../media/images/small/small_level_0_normal.png",
        starImgPaths_StarTecPro1: "../../media/images/small/small_level_1_normal.png",
        starImgPaths_StarTecPro2: "../../media/images/small/small_level_2_selected.png",
        starImgPaths_StarTecPro3: "../../media/images/small/small_level_3_normal.png"
      });
    },
    starTecPro3() {
      this.data.selectStarTecNum = 4;
      console.log(this.data.selectStarTecNum);
      this.setData({
        starImgPaths_StarTecPro0: "../../media/images/small/small_level_0_normal.png",
        starImgPaths_StarTecPro1: "../../media/images/small/small_level_1_normal.png",
        starImgPaths_StarTecPro2: "../../media/images/small/small_level_2_normal.png",
        starImgPaths_StarTecPro3: "../../media/images/small/small_level_3_selected.png"
      });
    },
    starEnvPro0() {
      this.data.selectTecEnvNum = 1;
      console.log(this.data.selectTecEnvNum);
      this.setData({
        starImgPaths_StarEnvPro0: "../../media/images/small/small_level_0_selected.png",
        starImgPaths_StarEnvPro1: "../../media/images/small/small_level_1_normal.png",
        starImgPaths_StarEnvPro2: "../../media/images/small/small_level_2_normal.png",
        starImgPaths_StarEnvPro3: "../../media/images/small/small_level_3_normal.png"
      });
    },
    starEnvPro1() {
      this.data.selectTecEnvNum = 2;
      console.log(this.data.selectTecEnvNum);
      this.setData({
        starImgPaths_StarEnvPro0: "../../media/images/small/small_level_0_normal.png",
        starImgPaths_StarEnvPro1: "../../media/images/small/small_level_1_selected.png",
        starImgPaths_StarEnvPro2: "../../media/images/small/small_level_2_normal.png",
        starImgPaths_StarEnvPro3: "../../media/images/small/small_level_3_normal.png"
      });
    },
    starEnvPro2() {
      this.data.selectTecEnvNum = 3;
      console.log(this.data.selectTecEnvNum);
      this.setData({
        starImgPaths_StarEnvPro0: "../../media/images/small/small_level_0_normal.png",
        starImgPaths_StarEnvPro1: "../../media/images/small/small_level_1_normal.png",
        starImgPaths_StarEnvPro2: "../../media/images/small/small_level_2_selected.png",
        starImgPaths_StarEnvPro3: "../../media/images/small/small_level_3_normal.png"
      });
    },
    starEnvPro3() {
      this.data.selectTecEnvNum = 4;
      console.log(this.data.selectTecEnvNum);
      this.setData({
        starImgPaths_StarEnvPro0: "../../media/images/small/small_level_0_normal.png",
        starImgPaths_StarEnvPro1: "../../media/images/small/small_level_1_normal.png",
        starImgPaths_StarEnvPro2: "../../media/images/small/small_level_2_normal.png",
        starImgPaths_StarEnvPro3: "../../media/images/small/small_level_3_selected.png"
      });
    },
    onCommit() {
      if(!this.data.hasUserInfo) {
        console.log("获取用户信息");
        this.getUserProfile();
        return;
      }
      let send_data = {
        proj_id: this.data.projIdArr[this.data.selectedProjIdx],
        tec_name: this.data.tecName,
        star_svr_num: this.data.selectStarSvrNum,
        star_tec_num: this.data.selectStarTecNum,
        star_env_num: this.data.selectStarEnvNum,
        content: this.data.sugContent,
        nick_name: this.data.userInfo.nickName,
        from_platform: 1,
        gender: this.data.userInfo.gender,
        language: this.data.userInfo.language,
        city: this.data.userInfo.city,
        province: this.data.userInfo.province,
        country: this.data.userInfo.country,
        avatar_url: this.data.userInfo.avatarUrl
      };
      console.log("提交内容: "  + JSON.stringify(send_data));
      wx.request({
        url: API.StartFeedback, // 接口地址
        method: 'POST', // 请求方法
        data: JSON.stringify(send_data),
        header: {
          'content-type': 'x-www-form-urlencoded' // 设置请求头
        },
        success(res) {
          console.log('请求成功:', res.data); // 打印返回数据
          if(res.data == '1') {
            wx.showModal({
              title: '尊敬的顾客',
              content: '感谢您的反馈和建议，我们将继续提升服务质量，欢迎下次光临！',
              showCancel: false
              });
          } else {
            wx.showModal({
              title: '提示',
              content: '没有提交成功，请重新提交',
              showCancel: false
              });
          }
        },
        fail(err) {
          console.error('请求失败:', err); // 打印错误信息
        }
        });
    }
  },
})
