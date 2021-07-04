package cn.itcast.handheldclass.Consumer;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.Toast;

import cn.itcast.handheldclass.BaseActivity;
import cn.itcast.handheldclass.Detail_text.PrivacyPolicyActivity;
import cn.itcast.handheldclass.R;
import cn.itcast.handheldclass.RegisterActivity;

public class ConsumerDesignerOwn4Activity extends BaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_consumer_designer_own4);
        initNavBar(true,"预约界面",false);

        //点击预约按钮
        Button yuyue= (Button) findViewById(R.id.image_designer_appointButton);
        yuyue.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){

                Toast.makeText(ConsumerDesignerOwn4Activity.this,"预约成功！",Toast.LENGTH_SHORT).show();
                Intent i = new Intent(ConsumerDesignerOwn4Activity.this , ConsumerChooseDerActivity.class);
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