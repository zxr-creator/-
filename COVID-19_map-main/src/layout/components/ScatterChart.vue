<template>
    <div id="scatter" style="height: 100%; width: 100%"></div>
  
</template>

<script>
import axios from 'axios'
import 'echarts' 
import VueEvent from '@/assets/utils/event'

export default {
  name: 'ScatterChart',
  data() {
      return {  
        scatterdata: [],
        network_movie:[],
        cinema_line:[]

      }
  },
  methods: {
      getdata() {
        // http://127.0.0.1:5000/api/getMsg
        var url = 'http://127.0.0.1:8002/api/getScatter'
        axios.get(url)
          .then((res) => {
            this.scatterdata = res.data.piedata;
            //console.log(this.scatterdata)
            var len = Math.max(this.scatterdata[0].network_movie.length,this.scatterdata[0].cinema_line.length)
            for (var i = 0; i < len; i++){
                this.network_movie.push(this.scatterdata[0].network_movie[i]);
                this.cinema_line.push(this.scatterdata[0].cinema_line[i])
                }
          })
          .catch((error) => {
            console.log(error);
          })
      },

    drawLine(myScatter){
        var that = this;
        
        //图表的配置项和数据
        var option = {             
          title: {
          text: '当月上映的网络/院线电影及票房情况',
          subtext: '气泡越大票房排名越高',
          left: 'center',
          textStyle:{
                color:'#8ec06c',
                frotSize:'40'
              }
        },
        legend: {
          right: '14%',
          top: '3%',
          data: ['院线电影', '网络电影']
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross'
          },
        },
        grid: {
          left: '8%',
          right:'12%',
          top: '25%',
          bottom:'10%'
        },
      xAxis: {
        type: 'category',
        data: [
          '1日','2日','3日','4日','5日','6日','7日','8日','9日','10日','11日','12日',
          '13日','14日','15日','16日','17日','18日','19日','20日','21日','22日','23日',
          '24日','25日','26日','27日','28日','29日','30日','31日'
        ],
        // minInterval: 1,
        splitLine: {
          lineStyle: {
            type: 'dashed'
          },
        },
        // 字体设置
        axisLabel:{
          type:"solid",
          color:"#56a0d3",
          fontSize:"12",
          nameLocation:'end'
          },
        // 坐标轴颜色
          axisLine:{
            color:'#56a0d3'
          }
      },
      yAxis: {
        name: '票房',
        nameTextStyle:{
            type:"solid",
            color:"#a25016",
            fontSize:"14"
        },
        type: 'value',
        axisLabel: {
          formatter: '{value}万元',
          type:"solid",
          color:"#d1de3f",
          fontSize:"12",
          nameLocation:'end'
        },
        splitLine: {
          lineStyle: {
            type: 'dashed'
          }
        },
        scale: true,
        // 坐标轴颜色
          axisLine:{
            color:'#56a0d3'
          }
      },

      series: [
        {
          data: that.cinema_line,
          name: '院线电影',
          type: 'scatter',
          symbolSize: function (data) {
            return data[2] * 6;
          },
          emphasis: {
            focus: 'series',
            label: {
              show: true,
              formatter: function (param) {
                return param.data[3];
              },
              position: 'top'
            }
          },
          itemStyle: {
            shadowBlur: 10,
            shadowColor: 'rgba(120, 36, 50, 0.5)',
            shadowOffsetY: 5,
            color: new this.$echarts.graphic.RadialGradient(0.4, 0.3, 1, [
              {
                offset: 0,
                color: '#e1306c'
              },
              {
                offset: 1,
                color: '#fd1d1d'
              }
            ])
          }
        },
        {
          name: '网络电影',
          data:that.network_movie,
          type: 'scatter',
          symbolSize: function (data) {
            return data[2] * 6;
          },
          emphasis: {
            focus: 'series',
            label: {
              show: true,
              formatter: function (param) {
                return param.data[3];
              },
              position: 'top'
            }
          },
          itemStyle: {
            shadowBlur: 10,
            shadowColor: 'rgba(25, 100, 150, 0.5)',
            shadowOffsetY: 5,
            color: new this.$echarts.graphic.RadialGradient(0.4, 0.3, 1, [
              {
                offset: 0,
                color: '#5851db'
              },
              {
                offset: 1,
                color: '#833ab4'
              }
            ])
          }
        }
      ]
        }; 
 
        //使用刚指定的配置项和数据显示图表。
        setTimeout(()=>{
        option && myScatter.setOption(option,true);
      },20) 

       VueEvent.on('timelinechanged',currentIndex =>{
         //console.log(currentIndex)
            that.network_movie = []
            that.cinema_line = []
            var len = Math.max(that.scatterdata[currentIndex].network_movie.length,that.scatterdata[currentIndex].cinema_line.length)
            for (var i = 0; i < len; i++){
                that.network_movie.push(that.scatterdata[currentIndex].network_movie[i]);
                if (that.scatterdata[currentIndex].cinema_line.length != 0)
                  that.cinema_line.push(that.scatterdata[currentIndex].cinema_line[i])
            }
            //console.log(option)
            //console.log(that.network_movie)
            setTimeout(()=>{
                myScatter.setOption({
                    series:[
                        {data: that.network_movie},
                        {data: that.cinema_line}
                    ]
                });
            },100) 
       })
    },
  },
    created(){
        this.getdata();
    },

    mounted(){
        var myScatter = this.$echarts.init(document.getElementById('scatter'));
        this.drawLine(myScatter);
  },
};


</script>

<style scoped>

</style>

