package cn.itcast.handheldclass.Consumer;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import cn.itcast.handheldclass.BaseActivity;
import cn.itcast.handheldclass.R;

public class ConsumerDesignerXxOwn2Activity extends BaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_consumer_designer_xx_own_2);
        initNavBar(true,"预约界面",false);

        //点击预约按钮
        Button yuyue= (Button) findViewById(R.id.image_designer_appointButton);
        yuyue.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){

                Toast.makeText(ConsumerDesignerXxOwn2Activity.this,"预约成功！",Toast.LENGTH_SHORT).show();
                Intent i = new Intent(ConsumerDesignerXxOwn2Activity.this , ConsumerChooseDer2Activity.class);
                //启动
                startActivity(i);
            }

        });

        //点击咨询按钮
        Button zixun= (Button) findViewById(R.id.image_designer_ask_Button);
        zixun.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                //函数



            }

        });
    }
}