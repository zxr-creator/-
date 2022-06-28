<template>
  <div id="line_race_chart" style="height: 100%; width: 100%"></div>

</template>

<script>
import * as echarts from "echarts"

export default {
  name: 'Line_race',
  data() {
    return {
    }
  },
  mounted() {
    var line_race_chart = echarts.init(document.getElementById("line_race_chart"));
    this.drawChart(line_race_chart);
  },

  methods: {

    drawChart(line_race_chart) {

      const seriesList = [];

      seriesList.push({
        data: [8.37,
          8.20,
          7.18,
          7.48,
          7.25,],
        type: "line",
        smooth: true,
        name: '剧情',
        showSymbol: false,
        endLabel: {
          show: true
        }
      });
      seriesList.push({
        data: [7.90,
          7.38,
          6.43,
          6.89,
          6.89],
        type: "line",
        smooth: true,
        name: '喜剧',
        showSymbol: false,
        endLabel: {
          show: true
        }
      })
      seriesList.push({
        data: [7.73,
          7.43,
          6.66,
          7.13,
          6.46,],
        type: "line",
        smooth: true,
        name: '动作',
        showSymbol: false,
        endLabel: {
          show: true
        }
      });
      seriesList.push({
        data: [7.73,
          7.43,
          6.66,
          7.13,
          6.46],
        type: "line",
        smooth: true,
        name: '爱情',
        showSymbol: false,
        endLabel: {
          show: true
        }
      });
      seriesList.push({
        data: [7.74,
          7.57,
          7.23,
          7.21,
          5.41],
        type: "line",
        smooth: true,
        name: '科幻',
        showSymbol: false,
        endLabel: {
          show: true
        }
      });
      seriesList.push({
        data: [7.70,
          7.79,
          7.73,
          7.46,
          7.84],
        type: "line",
        smooth: true,
        name: '动画',
        showSymbol: false,
        endLabel: {
          show: true
        }
      });
      seriesList.push({
        data: [6.81,
          6.47,
          6.19,
          7.10,
          7.20],
        type: "line",
        smooth: true,
        name: '悬疑',
        showSymbol: false,
        endLabel: {
          show: true
        }
      });
      setTimeout(() =>{
      line_race_chart.setOption({
        animationDuration: 10000,

        title: {
          text: '疫情前后豆瓣每年各类型电影加权评分',
          textStyle:{
                color:'#8ec06c',
                frotSize:'40'
              }
        },
        tooltip: {
          order: 'valueDesc',
          trigger: 'axis'
        },
        xAxis: {
          type: 'category',
          data:['2018年','2019年','2020年','2021年','2022年'],
          nameLocation: 'center',
          name: '年份',
          nameTextStyle:{
            type:"solid",
            color:"#a25016",
            fontSize:"14",
            padding:[10,0,0,0]
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
          name: '豆瓣评分（满分10分）',
          type:'value',
          min:5,
          max:10,
          interval:1,
          nameTextStyle:{
            type:"solid",
            color:"#a25016",
            fontSize:"14",
            padding:[0,40,0,100]
        },
        axisLabel:{
            type:"solid",
            color:"#774aa4",
            fontSize:"12",
            nameLocation:'end'
            },
          // 坐标轴颜色
          axisLine:{
            color:'#56a0d3'
          }
        },
        grid: {
          left:50,
          right:0,
          bottom:40
        },
        series: seriesList
      });
      },20)
    }

  },

};
</script>

<style scoped>

</style>
