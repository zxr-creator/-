<template>
    <div style="height: 100%; width: 100%" ref="map">
    </div>
</template>

<script> 
import chinaJson from '@/assets/china.json'
import axios from 'axios'
import 'echarts' 
import VueEvent from '@/assets/utils/event'

export default {
  name: "Map",
  data() {
    return{
      datas:[],
      temp:[],
    }
  },
  // 先获取后端数据
  
  methods: {
      getdata() {
        // 使用 axios 向 flask 发送请求
        const url = "http://127.0.0.1:8002/api/getMsg";
        
        this.$nextTick(function(){
          axios.get(url)
          .then((res) => {
            this.datas = res.data.province;
            //console.log(this.datas[0].name.length);
            for (var i = 0; i < this.datas[0].name.length; i++){
              this.temp.push({
                name:this.datas[0].name[i],
                value:this.datas[1].value[0][i],
              })
          }
        }).catch((error) => {
            console.log(error);
          })
      },
      )
      },

      MapInit(chart){
        var that = this;
  
        // 注册地图
        this.$echarts.registerMap('china', chinaJson)
      
        var option = {        
          // 引入时间轴
          timeline:{
            x:100,
            realtime:false,
            width: 670,
            axisType:'category',
            label:{
              color:'#56a0d3',
            },
            playInterval:2000,
            left:'20%',
          bottom:'6%',
          autoPlay: true,
          loop: true,
          //currentIndex:0

          data: ['2020.1','2020.2','2020.3','2020.4','2020.5','2020.6','2020.7','2020.8','2020.9','2020.10',
          '2020.11','2020.12','2021.1','2021.2','2021.3','2021.4','2021.5','2021.6','2021.7','2021.8','2021.9',
          '2021.10','2021.11','2021.12','2022.1','2022.2','2022.3'],
          tooltip:{
            // 显示触发类型, item 在 hover 时显示
              trigger: 'item',
              // 地图 : {b}（区域名称），{c}（合并数值）, {d}（无）
              formatter: '年月：{b}<br/> '
          }
        },
            // 图表标题和副标题
            title: {
              text: '当月新增确诊病例疫情地图',
              subtext: 'Data from website',
              sublink: 'https://ncov.dxy.cn/ncovh5/view/pneumonia',
              left:'15%',
              textStyle:{
                color:'#8ec06c',
                frotSize:'40'
              }
            },
            // 提示框组件
            tooltip: {
              // 显示触发类型, item 在 hover 时显示
              trigger: 'item',
              // 地图 : {b}（区域名称），{c}（合并数值）, {d}（无）
              formatter: '地区：{b}<br/> 新增确诊：{c} '
            },
            // 右侧工具栏
            toolbox: {
              show: true,
              orient: 'vertical',
              right: '0%',
              top: 'center',
              color:'#56a0d3',
              feature: {
                dataView: {readOnly: false},
                restore: {},
                saveAsImage: {},
                myTool1: {
                  show: true,
                  title: '返回全国数据',
                  icon: 'path://M432.45,595.444c0,2.177-4.661,6.82-11.305,6.82c-6.475,0-11.306-4.567-11.306-6.82s4.852-6.812,11.306-6.812C427.841,588.632,432.452,593.191,432.45,595.444L432.45,595.444z M421.155,589.876c-3.009,0-5.448,2.495-5.448,5.572s2.439,5.572,5.448,5.572c3.01,0,5.449-2.495,5.449-5.572C426.604,592.371,424.165,589.876,421.155,589.876L421.155,589.876z M421.146,591.891c-1.916,0-3.47,1.589-3.47,3.549c0,1.959,1.554,3.548,3.47,3.548s3.469-1.589,3.469-3.548C424.614,593.479,423.062,591.891,421.146,591.891L421.146,591.891zM421.146,591.891',
                  onclick: function (){
                      VueEvent.emit('blank')
                }
            },

              }
            },
            // 视觉映射组件
            visualMap: {
              min: 0,
              max: 1000,
              left: '20%',
              top: '30%',
              text: ['高','低'],
              calculable : true,
              hoverLink: true,
              inRange: {
                color: [
                  '#ffdc80',
                  '#fcaf45',
                  '#f77737',
                  '#f56040',
                  '#fd1d1d'
                ]
              },
            },
            series : [
              {
                name: '',
                type: 'map',
                map: 'china',
                // 地图位置调整
                layoutCenter: ['60%', '55%'],
                layoutSize: 650,
                // 鼠标缩放和平移漫游
                roam: true,
                itemStyle: {
                  normal:{
                    borderColor: 'rgba(0, 0, 0, 0.2)'
                  },
                  emphasis:{
                    shadowOffsetX: 0,
                    shadowOffsetY: 0,
                    shadowBlur: 20,
                    borderWidth: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                  }
                },
                showLegendSymbol: true,
                label: {
                  show: true,
                  emphasis: {
                    show: true
                  },  
                },

                // 地图数据
                data: this.temp,

                // 自定义名称映射
                nameMap: {
                  '香港特别行政区': '香港',
                  '澳门特别行政区': '澳门'
                }
              }
            ],
          }

      // 更新数据
      setTimeout(()=>{
        option && chart.setOption(option,true);
      },50) 

      // 检测时间轴事件变化
      chart.on('timelinechanged',function(timeLineIndx){
        //console.log(timeLineIndx);
        var res = timeLineIndx.currentIndex;

        // 更新数据
        //console.log(that.datas[1].value[res])
        that.temp = []
        for (var i = 0; i < that.datas[0].name.length; i++){
              that.temp.push({
                name:that.datas[0].name[i],
                value:that.datas[1].value[res][i]
              })
        }
        
        setTimeout(()=>{
          chart.setOption({
            series:[
              {data:that.temp}
            ]
          });
        },100)

        VueEvent.emit('timelinechanged',res)  

        // 点击省份联动
        chart.on('click',function(province){
        //var res = province.dataIndex
          if(province.data.name != undefined){
            VueEvent.emit('click',province)
          }
      })

    })
  },
  },

  created(){
    this.getdata();
  },

  mounted() {
     // 初始化echarts实例
    let chartDom = this.$refs.map
    let chart = this.$echarts.init(chartDom) 
    this.MapInit(chart);  
  },
}
</script>

<style scoped>

</style>
